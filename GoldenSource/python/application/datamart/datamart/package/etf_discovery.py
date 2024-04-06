### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from datamart_core.app.static.container import Container
from datamart_core.app.model.obbject import OBBject
from datamart_core.app.model.custom_parameter import DataMartCustomParameter
from typing import Optional, Literal
from typing_extensions import Annotated
from datamart_core.app.static.utils.decorators import exception_handler, validate

from datamart_core.app.static.utils.filters import filter_inputs


class ROUTER_etf_discovery(Container):
    """/etf/discovery
    active
    gainers
    losers
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @exception_handler
    @validate
    def active(
        self,
        sort: Annotated[
            Literal["asc", "desc"],
            DataMartCustomParameter(
                description="Sort order. Possible values: 'asc', 'desc'. Default: 'desc'."
            ),
        ] = "desc",
        limit: Annotated[
            int,
            DataMartCustomParameter(
                description="The number of data entries to return."
            ),
        ] = 10,
        provider: Annotated[
            Optional[Literal["wsj"]],
            DataMartCustomParameter(
                description="The provider to use for the query, by default None.\n    If None, the provider specified in defaults is selected or 'wsj' if there is\n    no default."
            ),
        ] = None,
        **kwargs
    ) -> OBBject:
        """Get the most active ETFs.

        Parameters
        ----------
        sort : Literal['asc', 'desc']
            Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.
        limit : int
            The number of data entries to return.
        provider : Optional[Literal['wsj']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'wsj' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[ETFActive]
                Serializable results.
            provider : Optional[Literal['wsj']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra : Dict[str, Any]
                Extra info.

        ETFActive
        ---------
        symbol : str
            Symbol representing the entity requested in the data.
        name : str
            Name of the entity.
        last_price : float
            Last price.
        percent_change : float
            Percent change.
        net_change : float
            Net change.
        volume : float
            The trading volume.
        date : date
            The date of the data.
        country : Optional[str]
            Country of the entity. (provider: wsj)
        mantissa : Optional[int]
            Mantissa. (provider: wsj)
        type : Optional[str]
            Type of the entity. (provider: wsj)
        formatted_price : Optional[str]
            Formatted price. (provider: wsj)
        formatted_volume : Optional[str]
            Formatted volume. (provider: wsj)
        formatted_price_change : Optional[str]
            Formatted price change. (provider: wsj)
        formatted_percent_change : Optional[str]
            Formatted percent change. (provider: wsj)
        url : Optional[str]
            The source url. (provider: wsj)

        Examples
        --------
        >>> from datamart import market
        >>> # Get the most active ETFs.
        >>> market.etf.discovery.active(provider='wsj')
        """  # noqa: E501

        return self._run(
            "/etf/discovery/active",
            **filter_inputs(
                provider_choices={
                    "provider": self._get_provider(
                        provider,
                        "/etf/discovery/active",
                        ("wsj",),
                    )
                },
                standard_params={
                    "sort": sort,
                    "limit": limit,
                },
                extra_params=kwargs,
            )
        )

    @exception_handler
    @validate
    def gainers(
        self,
        sort: Annotated[
            Literal["asc", "desc"],
            DataMartCustomParameter(
                description="Sort order. Possible values: 'asc', 'desc'. Default: 'desc'."
            ),
        ] = "desc",
        limit: Annotated[
            int,
            DataMartCustomParameter(
                description="The number of data entries to return."
            ),
        ] = 10,
        provider: Annotated[
            Optional[Literal["wsj"]],
            DataMartCustomParameter(
                description="The provider to use for the query, by default None.\n    If None, the provider specified in defaults is selected or 'wsj' if there is\n    no default."
            ),
        ] = None,
        **kwargs
    ) -> OBBject:
        """Get the top ETF gainers.

        Parameters
        ----------
        sort : Literal['asc', 'desc']
            Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.
        limit : int
            The number of data entries to return.
        provider : Optional[Literal['wsj']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'wsj' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[ETFGainers]
                Serializable results.
            provider : Optional[Literal['wsj']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra : Dict[str, Any]
                Extra info.

        ETFGainers
        ----------
        symbol : str
            Symbol representing the entity requested in the data.
        name : str
            Name of the entity.
        last_price : float
            Last price.
        percent_change : float
            Percent change.
        net_change : float
            Net change.
        volume : float
            The trading volume.
        date : date
            The date of the data.
        bluegrass_channel : Optional[str]
            Bluegrass channel. (provider: wsj)
        country : Optional[str]
            Country of the entity. (provider: wsj)
        mantissa : Optional[int]
            Mantissa. (provider: wsj)
        type : Optional[str]
            Type of the entity. (provider: wsj)
        formatted_price : Optional[str]
            Formatted price. (provider: wsj)
        formatted_volume : Optional[str]
            Formatted volume. (provider: wsj)
        formatted_price_change : Optional[str]
            Formatted price change. (provider: wsj)
        formatted_percent_change : Optional[str]
            Formatted percent change. (provider: wsj)
        url : Optional[str]
            The source url. (provider: wsj)

        Examples
        --------
        >>> from datamart import market
        >>> # Get the top ETF gainers.
        >>> market.etf.discovery.gainers(provider='wsj')
        """  # noqa: E501

        return self._run(
            "/etf/discovery/gainers",
            **filter_inputs(
                provider_choices={
                    "provider": self._get_provider(
                        provider,
                        "/etf/discovery/gainers",
                        ("wsj",),
                    )
                },
                standard_params={
                    "sort": sort,
                    "limit": limit,
                },
                extra_params=kwargs,
            )
        )

    @exception_handler
    @validate
    def losers(
        self,
        sort: Annotated[
            Literal["asc", "desc"],
            DataMartCustomParameter(
                description="Sort order. Possible values: 'asc', 'desc'. Default: 'desc'."
            ),
        ] = "desc",
        limit: Annotated[
            int,
            DataMartCustomParameter(
                description="The number of data entries to return."
            ),
        ] = 10,
        provider: Annotated[
            Optional[Literal["wsj"]],
            DataMartCustomParameter(
                description="The provider to use for the query, by default None.\n    If None, the provider specified in defaults is selected or 'wsj' if there is\n    no default."
            ),
        ] = None,
        **kwargs
    ) -> OBBject:
        """Get the top ETF losers.

        Parameters
        ----------
        sort : Literal['asc', 'desc']
            Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.
        limit : int
            The number of data entries to return.
        provider : Optional[Literal['wsj']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'wsj' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[ETFLosers]
                Serializable results.
            provider : Optional[Literal['wsj']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra : Dict[str, Any]
                Extra info.

        ETFLosers
        ---------
        symbol : str
            Symbol representing the entity requested in the data.
        name : str
            Name of the entity.
        last_price : float
            Last price.
        percent_change : float
            Percent change.
        net_change : float
            Net change.
        volume : float
            The trading volume.
        date : date
            The date of the data.
        bluegrass_channel : Optional[str]
            Bluegrass channel. (provider: wsj)
        country : Optional[str]
            Country of the entity. (provider: wsj)
        mantissa : Optional[int]
            Mantissa. (provider: wsj)
        type : Optional[str]
            Type of the entity. (provider: wsj)
        formatted_price : Optional[str]
            Formatted price. (provider: wsj)
        formatted_volume : Optional[str]
            Formatted volume. (provider: wsj)
        formatted_price_change : Optional[str]
            Formatted price change. (provider: wsj)
        formatted_percent_change : Optional[str]
            Formatted percent change. (provider: wsj)
        url : Optional[str]
            The source url. (provider: wsj)

        Examples
        --------
        >>> from datamart import market
        >>> # Get the top ETF losers.
        >>> market.etf.discovery.losers(provider='wsj')
        """  # noqa: E501

        return self._run(
            "/etf/discovery/losers",
            **filter_inputs(
                provider_choices={
                    "provider": self._get_provider(
                        provider,
                        "/etf/discovery/losers",
                        ("wsj",),
                    )
                },
                standard_params={
                    "sort": sort,
                    "limit": limit,
                },
                extra_params=kwargs,
            )
        )
