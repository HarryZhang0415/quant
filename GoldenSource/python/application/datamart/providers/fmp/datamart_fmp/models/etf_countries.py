"""FMP ETF Countries Model."""

import asyncio
from typing import Any, Dict, List, Optional
from warnings import warn

from datamart_core.provider.abstract.fetcher import Fetcher
from datamart_core.provider.standard_models.etf_countries import (
    EtfCountriesData,
    EtfCountriesQueryParams,
)
from datamart_core.provider.utils.errors import EmptyDataError
from datamart_core.provider.utils.helpers import amake_request
from datamart_fmp.utils.helpers import create_url, response_callback
from pandas import DataFrame


class FMPEtfCountriesQueryParams(EtfCountriesQueryParams):
    """FMP ETF Countries Query."""

    __json_schema_extra__ = {"symbol": ["multiple_items_allowed"]}


class FMPEtfCountriesData(EtfCountriesData):
    """FMP ETF Countries Data."""


class FMPEtfCountriesFetcher(
    Fetcher[
        FMPEtfCountriesQueryParams,
        List[FMPEtfCountriesData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPEtfCountriesQueryParams:
        """Transform the query."""
        return FMPEtfCountriesQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPEtfCountriesQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""
        symbols = query.symbol.split(",")
        results = {}

        async def get_one(symbol):
            """Get data for one symbol."""
            data = {}
            url = create_url(
                version=3,
                endpoint=f"etf-country-weightings/{symbol}",
                api_key=api_key,
            )
            result = await amake_request(
                url, response_callback=response_callback, **kwargs
            )

            if not result:
                warn(f"Symbol Error: No data found for {symbol}")

            if result:
                df = DataFrame(result).set_index("country")
                if len(df) > 0:
                    for i in df.index:
                        data.update(
                            {
                                i: float(df.loc[i]["weightPercentage"].replace("%", ""))
                                * 0.01
                            }
                        )
                    results.update({symbol: data})

        await asyncio.gather(*[get_one(symbol) for symbol in symbols])

        if not results:
            raise EmptyDataError("No data found for the given symbols.")

        output = (
            DataFrame(results)
            .transpose()
            .reset_index()
            .fillna(value=0)
            .replace(0, None)
            .rename(columns={"index": "symbol"})
        ).transpose()
        output.columns = output.loc["symbol"].to_list()  # type: ignore
        output = output.drop("symbol", axis=0).sort_values(
            by=output.columns[0], ascending=False
        )

        return (
            output.reset_index().rename(columns={"index": "country"}).to_dict("records")
        )

    @staticmethod
    def transform_data(
        query: FMPEtfCountriesQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPEtfCountriesData]:
        """Return the transformed data."""
        return [FMPEtfCountriesData.model_validate(d) for d in data]
