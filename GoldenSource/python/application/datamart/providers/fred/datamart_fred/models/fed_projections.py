"""FRED PROJECTION Model."""

from typing import Any, Dict, List, Optional

from datamart_core.provider.abstract.fetcher import Fetcher
from datamart_core.provider.standard_models.fed_projections import (
    PROJECTIONData,
    PROJECTIONQueryParams,
)
from datamart_fred.utils.fred_base import Fred
from datamart_fred.utils.fred_helpers import process_projections
from pydantic import Field

NAME_TO_ID_PROJECTION = {
    "range_high": ["FEDTARRH", "FEDTARRHLR"],
    "central_tendency_high": ["FEDTARCTH", "FEDTARCTHLR"],
    "median": ["FEDTARMD", "FEDTARMDLR"],
    "range_midpoint": ["FEDTARRM", "FEDTARRMLR"],
    "central_tendency_midpoint": ["FEDTARCTM", "FEDTARCTMLR"],
    "range_low": ["FEDTARRL", "FEDTARRLLR"],
    "central_tendency_low": ["FEDTARCTL", "FEDTARCTLLR"],
}


class FREDPROJECTIONQueryParams(PROJECTIONQueryParams):
    """FRED PROJECTION Query."""

    long_run: bool = Field(
        default=False, description="Flag to show long run projections"
    )


class FREDPROJECTIONData(PROJECTIONData):
    """FRED PROJECTION Data."""


class FREDPROJECTIONFetcher(
    Fetcher[FREDPROJECTIONQueryParams, List[Dict[str, List[FREDPROJECTIONData]]]]
):
    """Transform the query, extract and transform the data from the FRED endpoints."""

    data_type = FREDPROJECTIONData

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FREDPROJECTIONQueryParams:
        """Transform query."""
        return FREDPROJECTIONQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FREDPROJECTIONQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any
    ) -> list:
        """Extract data."""
        key = credentials.get("fred_api_key") if credentials else ""
        fred = Fred(key)
        data_dict = {}
        for key, value in NAME_TO_ID_PROJECTION.items():
            data = fred.get_series(value[query.long_run], **kwargs)
            data_dict[key] = data

        processed = process_projections(data_dict)

        return processed

    @staticmethod
    def transform_data(
        query: FREDPROJECTIONQueryParams, data: list, **kwargs: Any
    ) -> List[Dict[str, List[FREDPROJECTIONData]]]:
        """Transform data"""
        keys = ["date"] + list(NAME_TO_ID_PROJECTION.keys())
        return [FREDPROJECTIONData(**{k: x[k] for k in keys}) for x in data]
