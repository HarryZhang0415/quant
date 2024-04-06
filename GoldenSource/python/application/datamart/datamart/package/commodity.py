### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from datamart_core.app.static.container import Container
from datamart_core.app.model.obbject import OBBject
from datamart_core.app.model.custom_parameter import DataMartCustomParameter
import datetime
from typing import Union, Optional, Literal
from typing_extensions import Annotated
from datamart_core.app.static.utils.decorators import exception_handler, validate

from datamart_core.app.static.utils.filters import filter_inputs


class ROUTER_commodity(Container):
    """/commodity
    lbma_fixing
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @exception_handler
    @validate
    def lbma_fixing(
        self,
        asset: Annotated[
            Literal["gold", "silver"],
            DataMartCustomParameter(
                description="The metal to get price fixing rates for."
            ),
        ] = "gold",
        start_date: Annotated[
            Union[datetime.date, None, str],
            DataMartCustomParameter(
                description="Start date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        end_date: Annotated[
            Union[datetime.date, None, str],
            DataMartCustomParameter(
                description="Start date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        transform: Annotated[
            Literal["diff", "rdiff", "cumul", "normalize", None],
            DataMartCustomParameter(
                description="Transform the data as difference, percent change, cumulative, or normalize."
            ),
        ] = None,
        collapse: Annotated[
            Literal["daily", "weekly", "monthly", "quarterly", "annual", None],
            DataMartCustomParameter(
                description="Collapse the frequency of the time series."
            ),
        ] = None,
        provider: Annotated[
            Optional[Literal["nasdaq"]],
            DataMartCustomParameter(
                description="The provider to use for the query, by default None.\n    If None, the provider specified in defaults is selected or 'nasdaq' if there is\n    no default."
            ),
        ] = None,
        **kwargs
    ) -> OBBject:
        """Daily LBMA Fixing Prices in USD/EUR/GBP.

        Parameters
        ----------
        asset : Literal['gold', 'silver']
            The metal to get price fixing rates for.
        start_date : Union[datetime.date, None, str]
            Start date of the data, in YYYY-MM-DD format.
        end_date : Union[datetime.date, None, str]
            Start date of the data, in YYYY-MM-DD format.
        transform : Literal['diff', 'rdiff', 'cumul', 'normalize', None]
            Transform the data as difference, percent change, cumulative, or normalize.
        collapse : Literal['daily', 'weekly', 'monthly', 'quarterly', 'annual', None]
            Collapse the frequency of the time series.
        provider : Optional[Literal['nasdaq']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'nasdaq' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[LbmaFixing]
                Serializable results.
            provider : Optional[Literal['nasdaq']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra : Dict[str, Any]
                Extra info.

        LbmaFixing
        ----------
        date : date
            The date of the data.
        usd_am : Optional[float]
            AM fixing price in USD.
        usd_pm : Optional[float]
            PM fixing price in USD.
        gbp_am : Optional[float]
            AM fixing price in GBP.
        gbp_pm : Optional[float]
            PM fixing price in GBP.
        euro_am : Optional[float]
            AM fixing price in EUR.
        euro_pm : Optional[float]
            PM fixing price in EUR.
        usd : Optional[float]
            Daily fixing price in USD.
        gbp : Optional[float]
            Daily fixing price in GBP.
        eur : Optional[float]
            Daily fixing price in EUR.

        Examples
        --------
        >>> from datamart import market
        >>> market.commodity.lbma_fixing(provider='nasdaq')
        >>> # Get the daily LBMA fixing prices for silver in 2023.
        >>> market.commodity.lbma_fixing(asset='silver', start_date='2023-01-01', end_date='2023-12-31', transform='rdiff', collapse='monthly', provider='nasdaq')
        """  # noqa: E501

        return self._run(
            "/commodity/lbma_fixing",
            **filter_inputs(
                provider_choices={
                    "provider": self._get_provider(
                        provider,
                        "/commodity/lbma_fixing",
                        ("nasdaq",),
                    )
                },
                standard_params={
                    "asset": asset,
                    "start_date": start_date,
                    "end_date": end_date,
                    "transform": transform,
                    "collapse": collapse,
                },
                extra_params=kwargs,
            )
        )
