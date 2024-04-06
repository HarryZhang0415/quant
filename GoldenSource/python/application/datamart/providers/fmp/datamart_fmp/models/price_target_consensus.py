"""FMP Price Target Consensus Model."""

import asyncio
from typing import Any, Dict, List, Optional
from warnings import warn

from datamart_core.provider.abstract.fetcher import Fetcher
from datamart_core.provider.standard_models.price_target_consensus import (
    PriceTargetConsensusData,
    PriceTargetConsensusQueryParams,
)
from datamart_core.provider.utils.errors import EmptyDataError
from datamart_core.provider.utils.helpers import amake_request
from datamart_fmp.utils.helpers import create_url, response_callback


class FMPPriceTargetConsensusQueryParams(PriceTargetConsensusQueryParams):
    """FMP Price Target Consensus Query.

    Source: https://site.financialmodelingprep.com/developer/docs/price-target-consensus-api/
    """

    __json_schema_extra__ = {"symbol": ["multiple_items_allowed"]}


class FMPPriceTargetConsensusData(PriceTargetConsensusData):
    """FMP Price Target Consensus Data."""


class FMPPriceTargetConsensusFetcher(
    Fetcher[
        FMPPriceTargetConsensusQueryParams,
        List[FMPPriceTargetConsensusData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPPriceTargetConsensusQueryParams:
        """Transform the query params."""
        return FMPPriceTargetConsensusQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPPriceTargetConsensusQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        symbols = query.symbol.split(",")
        results = []

        async def get_one(symbol):
            """Get data for one symbol."""
            url = create_url(
                4, "price-target-consensus", api_key, query, exclude=["symbol"]
            )
            url = f"{url}&symbol={symbol}"
            result = await amake_request(
                url, response_callback=response_callback, **kwargs
            )
            if not result or len(result) == 0:
                warn(f"Symbol Error: No data found for {symbol}")
            if result:
                results.extend(result)

        await asyncio.gather(*[get_one(symbol) for symbol in symbols])

        if not results:
            raise EmptyDataError("No data returned for the given symbols.")

        return sorted(
            results,
            key=(lambda item: (symbols.index(item.get("symbol", len(symbols))))),
        )

    @staticmethod
    def transform_data(
        query: FMPPriceTargetConsensusQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[FMPPriceTargetConsensusData]:
        """Return the transformed data."""
        return [FMPPriceTargetConsensusData.model_validate(d) for d in data]
