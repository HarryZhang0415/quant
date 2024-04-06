"""Benzinga Company News Model."""

import math
from datetime import (
    date as dateType,
    datetime,
)
from typing import Any, Dict, List, Literal, Optional

from datamart_core.provider.abstract.fetcher import Fetcher
from datamart_core.provider.standard_models.company_news import (
    CompanyNewsData,
    CompanyNewsQueryParams,
)
from datamart_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from datamart_core.provider.utils.helpers import amake_requests, get_querystring
from pydantic import Field, field_validator


class BenzingaCompanyNewsQueryParams(CompanyNewsQueryParams):
    """Benzinga Company News Query.

    Source: https://docs.benzinga.io/benzinga/newsfeed-v2.html
    """

    __alias_dict__ = {
        "symbol": "tickers",
        "display": "displayOutput",
        "limit": "pageSize",
        "start_date": "dateFrom",
        "end_date": "dateTo",
        "updated_since": "updatedSince",
        "published_since": "publishedSince",
    }
    __json_schema_extra__ = {"symbol": ["multiple_items_allowed"]}

    date: Optional[dateType] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("date", "")
    )
    display: Literal["headline", "abstract", "full"] = Field(
        default="full",
        description="Specify headline only (headline), headline + teaser (abstract), or headline + full body (full).",
    )
    updated_since: Optional[int] = Field(
        default=None,
        description="Number of seconds since the news was updated.",
    )
    published_since: Optional[int] = Field(
        default=None,
        description="Number of seconds since the news was published.",
    )

    sort: Literal["id", "created", "updated"] = Field(
        default="created", description="Key to sort the news by."
    )
    order: Literal["asc", "desc"] = Field(
        default="desc", description="Order to sort the news by."
    )
    isin: Optional[str] = Field(default=None, description="The company's ISIN.")
    cusip: Optional[str] = Field(default=None, description="The company's CUSIP.")
    channels: Optional[str] = Field(
        default=None, description="Channels of the news to retrieve."
    )
    topics: Optional[str] = Field(
        default=None, description="Topics of the news to retrieve."
    )
    authors: Optional[str] = Field(
        default=None, description="Authors of the news to retrieve."
    )
    content_types: Optional[str] = Field(
        default=None, description="Content types of the news to retrieve."
    )


class BenzingaCompanyNewsData(CompanyNewsData):
    """Benzinga Company News Data."""

    __alias_dict__ = {
        "symbols": "stocks",
        "date": "created",
        "text": "body",
        "images": "image",
    }

    id: str = Field(description="Article ID.")
    author: Optional[str] = Field(default=None, description="Author of the article.")
    teaser: Optional[str] = Field(description="Teaser of the news.", default=None)
    images: Optional[List[Dict[str, str]]] = Field(
        default=None, description="URL to the images of the news."
    )
    channels: Optional[str] = Field(
        default=None,
        description="Channels associated with the news.",
    )
    stocks: Optional[str] = Field(
        description="Stocks associated with the news.",
        default=None,
    )
    tags: Optional[str] = Field(
        description="Tags associated with the news.",
        default=None,
    )
    updated: Optional[datetime] = Field(
        default=None, description="Updated date of the news."
    )

    @field_validator("symbols", mode="before", check_fields=False)
    @classmethod
    def symbols_string(cls, v):
        """Symbols string validator."""
        return ",".join([item["name"] for item in v])

    @field_validator("date", "updated", mode="before", check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return the date as a datetime object."""
        return datetime.strptime(v, "%a, %d %b %Y %H:%M:%S %z")

    @field_validator("stocks", "channels", "tags", mode="before", check_fields=False)
    def list_validate(cls, v):  # pylint: disable=E0213
        """Return the list as a string."""
        return ",".join(
            [item.get("name", None) for item in v if item.get("name", None)]
        )

    @field_validator("id", mode="before", check_fields=False)
    def id_validate(cls, v):  # pylint: disable=E0213
        """Return the id as a string."""
        return str(v)


class BenzingaCompanyNewsFetcher(
    Fetcher[
        BenzingaCompanyNewsQueryParams,
        List[BenzingaCompanyNewsData],
    ]
):
    """Transform the query, extract and transform the data from the Benzinga endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> BenzingaCompanyNewsQueryParams:
        """Transform query params."""
        return BenzingaCompanyNewsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: BenzingaCompanyNewsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract data."""
        token = credentials.get("benzinga_api_key") if credentials else ""

        base_url = "https://api.benzinga.com/api/v2/news"

        query.sort = f"{query.sort}:{query.order}" if query.sort and query.order else ""
        querystring = get_querystring(
            query.model_dump(by_alias=True), ["order", "pageSize"]
        )

        pages = math.ceil(query.limit / 100) if query.limit else 1
        page_size = 100 if query.limit and query.limit > 100 else query.limit
        urls = [
            f"{base_url}?{querystring}&page={page}&pageSize={page_size}&token={token}"
            for page in range(pages)
        ]

        data = await amake_requests(urls, **kwargs)

        return data[: query.limit]

    # pylint: disable=unused-argument
    @staticmethod
    def transform_data(
        query: BenzingaCompanyNewsQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[BenzingaCompanyNewsData]:
        """Transform data."""
        return [BenzingaCompanyNewsData.model_validate(item) for item in data]
