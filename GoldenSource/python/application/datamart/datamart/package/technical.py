### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from datamart_core.app.static.container import Container
from datamart_core.app.model.obbject import OBBject
from datamart_core.app.model.custom_parameter import DataMartCustomParameter
import pandas
import numpy
from typing import List, Union, Optional, Literal
from annotated_types import Ge, Gt
from typing_extensions import Annotated
from datamart_core.app.static.utils.decorators import exception_handler, validate

from datamart_core.app.static.utils.filters import filter_inputs

from datamart_core.provider.abstract.data import Data


class ROUTER_technical(Container):
    """/technical
    ad
    adosc
    adx
    aroon
    atr
    bbands
    cci
    cg
    clenow
    cones
    demark
    donchian
    ema
    fib
    fisher
    hma
    ichimoku
    kc
    macd
    obv
    rsi
    sma
    stoch
    vwap
    wma
    zlma
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def ad(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        offset: int = 0,
    ) -> OBBject:
        """Calculate the Accumulation/Distribution Line.

        Similar to the On Balance Volume (OBV).
        Sums the volume times +1/-1 based on whether the close is higher than the previous
        close. The Accumulation/Distribution indicator, however multiplies the volume by the
        close location value (CLV). The CLV is based on the movement of the issue within a
        single bar and can be +1, -1 or zero.


        The Accumulation/Distribution Line is interpreted by looking for a divergence in
        the direction of the indicator relative to price. If the Accumulation/Distribution
        Line is trending upward it indicates that the price may follow. Also, if the
        Accumulation/Distribution Line becomes flat while the price is still rising (or falling)
        then it signals an impending flattening of the price.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        offset : int, optional
            Offset of the AD, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Accumulation/Distribution Line.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> ad_data = market.technical.ad(data=stock_data.results, offset=0)
        >>> market.technical.ad(data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/ad",
            **filter_inputs(
                data=data,
                index=index,
                offset=offset,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def adosc(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        fast: Annotated[int, Gt(gt=0)] = 3,
        slow: Annotated[int, Gt(gt=0)] = 10,
        offset: int = 0,
    ) -> OBBject:
        """Calculate the Accumulation/Distribution Oscillator.

        Also known as the Chaikin Oscillator.

        Essentially a momentum indicator, but of the Accumulation-Distribution line
        rather than merely price. It looks at both the strength of price moves and the
        underlying buying and selling pressure during a given time period. The oscillator
        reading above zero indicates net buying pressure, while one below zero registers
        net selling pressure. Divergence between the indicator and pure price moves are
        the most common signals from the indicator, and often flag market turning points.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        fast : PositiveInt, optional
            Number of periods to be used for the fast calculation, by default 3.
        slow : PositiveInt, optional
            Number of periods to be used for the slow calculation, by default 10.
        offset : int, optional
            Offset to be used for the calculation, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Accumulation/Distribution Oscillator.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> adosc_data = market.technical.adosc(data=stock_data.results, fast=3, slow=10, offset=0)
        >>> market.technical.adosc(fast=2, slow=4, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/adosc",
            **filter_inputs(
                data=data,
                index=index,
                fast=fast,
                slow=slow,
                offset=offset,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def adx(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: int = 50,
        scalar: float = 100.0,
        drift: int = 1,
        chart: Annotated[
            bool,
            DataMartCustomParameter(
                description="Whether to create a chart or not, by default False."
            ),
        ] = False,
    ) -> OBBject:
        """Calculate the Average Directional Index (ADX).

        The ADX is a Welles Wilder style moving average of the Directional Movement Index (DX).
        The values range from 0 to 100, but rarely get above 60. To interpret the ADX, consider
        a high number to be a strong trend, and a low number, a weak trend.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            Number of periods for the ADX, by default 50.
        scalar : float, optional
            Scalar value for the ADX, by default 100.0.
        drift : int, optional
            Drift value for the ADX, by default 1.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Average Directional Index (ADX).
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> adx_data = market.technical.adx(data=stock_data.results, length=50, scalar=100.0, drift=1)
        >>> market.technical.adx(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/adx",
            **filter_inputs(
                data=data,
                index=index,
                length=length,
                scalar=scalar,
                drift=drift,
                chart=chart,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def aroon(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: int = 25,
        scalar: int = 100,
        chart: Annotated[
            bool,
            DataMartCustomParameter(
                description="Whether to create a chart or not, by default False."
            ),
        ] = False,
    ) -> OBBject:
        """Calculate the Aroon Indicator.

        The word aroon is Sanskrit for "dawn's early light." The Aroon
        indicator attempts to show when a new trend is dawning. The indicator consists
        of two lines (Up and Down) that measure how long it has been since the highest
        high/lowest low has occurred within an n period range.

        When the Aroon Up is staying between 70 and 100 then it indicates an upward trend.
        When the Aroon Down is staying between 70 and 100 then it indicates an downward trend.
        A strong upward trend is indicated when the Aroon Up is above 70 while the Aroon Down is below 30.
        Likewise, a strong downward trend is indicated when the Aroon Down is above 70 while
        the Aroon Up is below 30. Also look for crossovers. When the Aroon Down crosses above
        the Aroon Up, it indicates a weakening of the upward trend (and vice versa).

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index: str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            Number of periods to be used for the calculation, by default 25.
        scalar : int, optional
            Scalar to be used for the calculation, by default 100.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Chande Momentum Oscillator.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> aaron_data = market.technical.aroon(data=stock_data.results, length=25, scalar=100)
        >>> market.technical.aroon(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/aroon",
            **filter_inputs(
                data=data,
                index=index,
                length=length,
                scalar=scalar,
                chart=chart,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def atr(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: Annotated[int, Gt(gt=0)] = 14,
        mamode: Literal["rma", "ema", "sma", "wma"] = "rma",
        drift: Annotated[int, Ge(ge=0)] = 1,
        offset: int = 0,
    ) -> OBBject:
        """Calculate the Average True Range.

        Used to measure volatility, especially volatility caused by gaps or limit moves.
        The ATR metric helps understand how much the values in your data change on average,
        giving insights into the stability or unpredictability during a certain period.
        It's particularly useful for spotting trends of increase or decrease in variations,
        without getting into technical trading details.
        The method considers not just the day-to-day changes but also accounts for any
        sudden jumps or drops, ensuring you get a comprehensive view of movement.

        Parameters
        ----------
        data : List[Data]
            List of data to apply the indicator to.
        index : str, optional
            Index column name, by default "date"
        length : PositiveInt, optional
            It's period, by default 14
        mamode : Literal["rma", "ema", "sma", "wma"], optional
            Moving average mode, by default "rma"
        drift : NonNegativeInt, optional
            The difference period, by default 1
        offset : int, optional
            How many periods to offset the result, by default 0

        Returns
        -------
        OBBject[List[Data]]
            List of data with the indicator applied.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Average True Range.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> atr_data = market.technical.atr(data=stock_data.results)
        >>> market.technical.atr(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/atr",
            **filter_inputs(
                data=data,
                index=index,
                length=length,
                mamode=mamode,
                drift=drift,
                offset=offset,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def bbands(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 50,
        std: Annotated[float, Ge(ge=0)] = 2,
        mamode: Literal["sma", "ema", "wma", "rma"] = "sma",
        offset: int = 0,
    ) -> OBBject:
        """Calculate the Bollinger Bands.

        Consist of three lines. The middle band is a simple moving average (generally 20
        periods) of the typical price (TP). The upper and lower bands are F standard
        deviations (generally 2) above and below the middle band.
        The bands widen and narrow when the volatility of the price is higher or lower,
        respectively.

        Bollinger Bands do not, in themselves, generate buy or sell signals;
        they are an indicator of overbought or oversold conditions. When the price is near the
        upper or lower band it indicates that a reversal may be imminent. The middle band
        becomes a support or resistance level. The upper and lower bands can also be
        interpreted as price targets. When the price bounces off of the lower band and crosses
        the middle band, then the upper band becomes the price target.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            Number of periods to be used for the calculation, by default 50.
        std : NonNegativeFloat, optional
            Standard deviation to be used for the calculation, by default 2.
        mamode : Literal["sma", "ema", "wma", "rma"], optional
            Moving average mode to be used for the calculation, by default "sma".
        offset : int, optional
            Offset to be used for the calculation, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Chande Momentum Oscillator.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> bbands_data = market.technical.bbands(data=stock_data.results, target='close', length=50, std=2, mamode='sma')
        >>> market.technical.bbands(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/bbands",
            **filter_inputs(
                data=data,
                target=target,
                index=index,
                length=length,
                std=std,
                mamode=mamode,
                offset=offset,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def cci(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: Annotated[int, Gt(gt=0)] = 14,
        scalar: Annotated[float, Gt(gt=0)] = 0.015,
    ) -> OBBject:
        """Calculate the Commodity Channel Index (CCI).

        The CCI is designed to detect beginning and ending market trends.
        The range of 100 to -100 is the normal trading range. CCI values outside of this
        range indicate overbought or oversold conditions. You can also look for price
        divergence in the CCI. If the price is making new highs, and the CCI is not,
        then a price correction is likely.

        Parameters
        ----------
        data : List[Data]
            The data to use for the CCI calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : PositiveInt, optional
            The length of the CCI, by default 14.
        scalar : PositiveFloat, optional
            The scalar of the CCI, by default 0.015.

        Returns
        -------
        OBBject[List[Data]]
            The CCI data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Commodity Channel Index (CCI).
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> cci_data = market.technical.cci(data=stock_data.results, length=14, scalar=0.015)
        >>> market.technical.cci(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/cci",
            **filter_inputs(
                data=data,
                index=index,
                length=length,
                scalar=scalar,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def cg(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: Annotated[int, Gt(gt=0)] = 14,
    ) -> OBBject:
        """Calculate the Center of Gravity.

        The Center of Gravity indicator, in short, is used to anticipate future price movements
        and to trade on price reversals as soon as they happen. However, just like other oscillators,
        the COG indicator returns the best results in range-bound markets and should be avoided when
        the price is trending. Traders who use it will be able to closely speculate the upcoming
        price change of the asset.

        Parameters
        ----------
        data : List[Data]
            The data to use for the COG calculation.
        index : str, optional
            Index column name to use with `data`, by default "date"
        length : PositiveInt, optional
            The length of the COG, by default 14

        Returns
        -------
        OBBject[List[Data]]
            The COG data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Center of Gravity (CG).
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> cg_data = market.technical.cg(data=stock_data.results, length=14)
        >>> market.technical.cg(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/cg",
            **filter_inputs(
                data=data,
                index=index,
                length=length,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def clenow(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        target: str = "close",
        period: Annotated[int, Gt(gt=0)] = 90,
    ) -> OBBject:
        """Calculate the Clenow Volatility Adjusted Momentum.

        The Clenow Volatility Adjusted Momentum is a sophisticated approach to understanding market momentum with a twist.
        It adjusts for volatility, offering a clearer picture of true momentum by considering how price movements are
        influenced by their volatility over a set period. It helps in identifying stronger, more reliable trends.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        target : str, optional
            Target column name, by default "close".
        period : PositiveInt, optional
            Number of periods for the momentum, by default 90.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Clenow Volatility Adjusted Momentum.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> clenow_data = market.technical.clenow(data=stock_data.results, period=90)
        >>> market.technical.clenow(period=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/clenow",
            **filter_inputs(
                data=data,
                index=index,
                target=target,
                period=period,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def cones(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        lower_q: float = 0.25,
        upper_q: float = 0.75,
        model: Literal[
            "std",
            "parkinson",
            "garman_klass",
            "hodges_tompkins",
            "rogers_satchell",
            "yang_zhang",
        ] = "std",
        is_crypto: bool = False,
        trading_periods: Optional[int] = None,
        chart: Annotated[
            bool,
            DataMartCustomParameter(
                description="Whether to create a chart or not, by default False."
            ),
        ] = False,
    ) -> OBBject:
        """Calculate the realized volatility quantiles over rolling windows of time.

        The cones indicator is designed to map out the ebb and flow of price movements through a detailed analysis of
        volatility quantiles. By examining the range of volatility within specific time frames, it offers a nuanced view of
        market behavior, highlighting periods of stability and turbulence.

        The model for calculating volatility is selectable and can be one of the following:
        - Standard deviation
        - Parkinson
        - Garman-Klass
        - Hodges-Tompkins
        - Rogers-Satchell
        - Yang-Zhang

        Read more about it in the model parameter description.

        Parameters
        ----------
        data : List[Data]
            The data to use for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date"
        lower_q : float, optional
            The lower quantile value for calculations
        upper_q : float, optional
            The upper quantile value for calculations
        model : Literal["std", "parkinson", "garman_klass", "hodges_tompkins", "rogers_satchell", "yang_zhang"], optional
            The model used to calculate realized volatility

                Standard deviation measures how widely returns are dispersed from the average return.
                It is the most common (and biased) estimator of volatility.

                Parkinson volatility uses the high and low price of the day rather than just close to close prices.
                It is useful for capturing large price movements during the day.

                Garman-Klass volatility extends Parkinson volatility by taking into account the opening and closing price.
                As markets are most active during the opening and closing of a trading session;
                it makes volatility estimation more accurate.

                Hodges-Tompkins volatility is a bias correction for estimation using an overlapping data sample.
                It produces unbiased estimates and a substantial gain in efficiency.

                Rogers-Satchell is an estimator for measuring the volatility with an average return not equal to zero.
                Unlike Parkinson and Garman-Klass estimators, Rogers-Satchell incorporates a drift term,
                mean return not equal to zero.

                Yang-Zhang volatility is the combination of the overnight (close-to-open volatility).
                It is a weighted average of the Rogers-Satchell volatility and the open-to-close volatility.
        is_crypto : bool, optional
            Whether the data is crypto or not. If True, volatility is calculated for 365 days instead of 252
        trading_periods : Optional[int] [default: 252]
            Number of trading periods in a year.

        Returns
        -------
        OBBject[List[Data]]
            The cones data.

        Examples
        --------
        >>> from datamart import market
        >>> # Realized Volatility Cones.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='yfinance')
        >>> cones_data = market.technical.cones(data=stock_data.results, lower_q=0.25, upper_q=0.75, model='std')
        >>> market.technical.cones(data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/cones",
            **filter_inputs(
                data=data,
                index=index,
                lower_q=lower_q,
                upper_q=upper_q,
                model=model,
                is_crypto=is_crypto,
                trading_periods=trading_periods,
                chart=chart,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def demark(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        target: str = "close",
        show_all: bool = True,
        asint: bool = True,
        offset: int = 0,
    ) -> OBBject:
        """Calculate the Demark sequential indicator.

        This indicator offers a strategic way to spot potential reversals in market trends.
        It's designed to highlight moments when the current trend may be running out of steam,
        suggesting a possible shift in direction. By focusing on specific patterns in price movements, it provides
        valuable insights for making informed decisions on future changes and identifies trend exhaustion points
        with precision.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        target : str, optional
            Target column name, by default "close".
        show_all : bool, optional
            Show 1 - 13. If set to False, show 6 - 9
        asint : bool, optional
            If True, fill NAs with 0 and change type to int, by default True.
        offset : int, optional
            How many periods to offset the result

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Demark Sequential Indicator.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> demark_data = market.technical.demark(data=stock_data.results, offset=0)
        >>> market.technical.demark(data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/demark",
            **filter_inputs(
                data=data,
                index=index,
                target=target,
                show_all=show_all,
                asint=asint,
                offset=offset,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def donchian(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        lower_length: Annotated[int, Gt(gt=0)] = 20,
        upper_length: Annotated[int, Gt(gt=0)] = 20,
        offset: int = 0,
    ) -> OBBject:
        """Calculate the Donchian Channels.

        Three lines generated by moving average calculations that comprise an indicator
        formed by upper and lower bands around a midrange or median band. The upper band
        marks the highest price of a security over N periods while the lower band
        marks the lowest price of a security over N periods. The area
        between the upper and lower bands represents the Donchian Channel.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        lower_length : PositiveInt, optional
            Number of periods for the lower band, by default 20.
        upper_length : PositiveInt, optional
            Number of periods for the upper band, by default 20.
        offset : int, optional
            Offset of the Donchian Channel, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Donchian Channels.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> donchian_data = market.technical.donchian(data=stock_data.results, lower_length=20, upper_length=20, offset=0)
        >>> market.technical.donchian(lower_length=1, upper_length=3, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/donchian",
            **filter_inputs(
                data=data,
                index=index,
                lower_length=lower_length,
                upper_length=upper_length,
                offset=offset,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def ema(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 50,
        offset: int = 0,
        chart: Annotated[
            bool,
            DataMartCustomParameter(
                description="Whether to create a chart or not, by default False."
            ),
        ] = False,
    ) -> OBBject:
        """Calculate the Exponential Moving Average (EMA).

        EMA is a cumulative calculation, including all data. Past values have
        a diminishing contribution to the average, while more recent values have a greater
        contribution. This method allows the moving average to be more responsive to changes
        in the data.

        Parameters
        ----------
        data : List[Data]
            The data to use for the calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date"
        length : int, optional
            The length of the calculation, by default 50.
        offset : int, optional
            The offset of the calculation, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Exponential Moving Average (EMA).
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> ema_data = market.technical.ema(data=stock_data.results, target='close', length=50, offset=0)
        >>> market.technical.ema(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/ema",
            **filter_inputs(
                data=data,
                target=target,
                index=index,
                length=length,
                offset=offset,
                chart=chart,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def fib(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        close_column: Literal["close", "adj_close"] = "close",
        period: Annotated[int, Gt(gt=0)] = 120,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> OBBject:
        """Create Fibonacci Retracement Levels.

        This method draws from a classic technique to pinpoint significant price levels
        that often indicate where the market might find support or resistance.
        It's a tool used to gauge potential turning points in the data by applying a
        mathematical approach rooted in nature's patterns. Is used to get insights into
        where prices could head next, based on historical movements.

        Parameters
        ----------
        data : List[Data]
            List of data to apply the indicator to.
        index : str, optional
            Index column name, by default "date"
        period : PositiveInt, optional
            Period to calculate the indicator, by default 120

        Returns
        -------
        OBBject[List[Data]]
            List of data with the indicator applied.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Bollinger Band Width.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> fib_data = market.technical.fib(data=stock_data.results, period=120)
        >>> market.technical.fib(data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/fib",
            **filter_inputs(
                data=data,
                index=index,
                close_column=close_column,
                period=period,
                start_date=start_date,
                end_date=end_date,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def fisher(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: Annotated[int, Gt(gt=0)] = 14,
        signal: Annotated[int, Gt(gt=0)] = 1,
    ) -> OBBject:
        """Perform the Fisher Transform.

        A technical indicator created by John F. Ehlers that converts prices into a Gaussian
        normal distribution. The indicator highlights when prices have moved to an extreme,
        based on recent prices.
        This may help in spotting turning points in the price of an asset. It also helps
        show the trend and isolate the price waves within a trend.

        Parameters
        ----------
        data : List[Data]
            List of data to apply the indicator to.
        index : str, optional
            Index column name, by default "date"
        length : PositiveInt, optional
            Fisher period, by default 14
        signal : PositiveInt, optional
            Fisher Signal period, by default 1

        Returns
        -------
        OBBject[List[Data]]
            List of data with the indicator applied.

        Examples
        --------
        >>> from datamart import market
        >>> # Perform the Fisher Transform.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> fisher_data = market.technical.fisher(data=stock_data.results, length=14, signal=1)
        >>> market.technical.fisher(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/fisher",
            **filter_inputs(
                data=data,
                index=index,
                length=length,
                signal=signal,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def hma(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 50,
        offset: int = 0,
        chart: Annotated[
            bool,
            DataMartCustomParameter(
                description="Whether to create a chart or not, by default False."
            ),
        ] = False,
    ) -> OBBject:
        """Calculate the Hull Moving Average (HMA).

        Solves the age old dilemma of making a moving average more responsive to current
        price activity whilst maintaining curve smoothness.
        In fact the HMA almost eliminates lag altogether and manages to improve smoothing
        at the same time.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            Number of periods for the HMA, by default 50.
        offset : int, optional
            Offset of the HMA, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Calculate HMA with historical stock data.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> hma_data = market.technical.hma(data=stock_data.results, target='close', length=50, offset=0)
        """  # noqa: E501

        return self._run(
            "/technical/hma",
            **filter_inputs(
                data=data,
                target=target,
                index=index,
                length=length,
                offset=offset,
                chart=chart,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def ichimoku(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        conversion: Annotated[int, Gt(gt=0)] = 9,
        base: Annotated[int, Gt(gt=0)] = 26,
        lagging: Annotated[int, Gt(gt=0)] = 52,
        offset: Annotated[int, Gt(gt=0)] = 26,
        lookahead: bool = False,
    ) -> OBBject:
        """Calculate the Ichimoku Cloud.

        Also known as Ichimoku Kinko Hyo, is a versatile indicator that defines support and
        resistance, identifies trend direction, gauges momentum and provides trading
        signals. Ichimoku Kinko Hyo translates into "one look equilibrium chart". With
        one look, chartists can identify the trend and look for potential signals within
        that trend.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        conversion : PositiveInt, optional
            Number of periods for the conversion line, by default 9.
        base : PositiveInt, optional
            Number of periods for the base line, by default 26.
        lagging : PositiveInt, optional
            Number of periods for the lagging span, by default 52.
        offset : PositiveInt, optional
            Number of periods for the offset, by default 26.
        lookahead : bool, optional
            drops the Chikou Span Column to prevent potential data leak

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Ichimoku Cloud.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> ichimoku_data = market.technical.ichimoku(data=stock_data.results, conversion=9, base=26, lookahead=False)
        """  # noqa: E501

        return self._run(
            "/technical/ichimoku",
            **filter_inputs(
                data=data,
                index=index,
                conversion=conversion,
                base=base,
                lagging=lagging,
                offset=offset,
                lookahead=lookahead,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def kc(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: Annotated[int, Gt(gt=0)] = 20,
        scalar: Annotated[float, Gt(gt=0)] = 20,
        mamode: Literal["ema", "sma", "wma", "hma", "zlma"] = "ema",
        offset: Annotated[int, Ge(ge=0)] = 0,
    ) -> OBBject:
        """Calculate the Keltner Channels.

        Keltner Channels are volatility-based bands that are placed
        on either side of an asset's price and can aid in determining
        the direction of a trend.The Keltner channel uses the average
        true range (ATR) or volatility, with breaks above or below the top
        and bottom barriers signaling a continuation.

        Parameters
        ----------
        data : List[Data]
            The data to use for the Keltner Channels calculation.
        index : str, optional
            Index column name to use with `data`, by default "date"
        length : PositiveInt, optional
            The length of the Keltner Channels, by default 20
        scalar : PositiveFloat, optional
            The scalar to use for the Keltner Channels, by default 20
        mamode : Literal["ema", "sma", "wma", "hma", "zlma"], optional
            The moving average mode to use for the Keltner Channels, by default "ema"
        offset : NonNegativeInt, optional
            The offset to use for the Keltner Channels, by default 0

        Returns
        -------
        OBBject[List[Data]]
            The Keltner Channels data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Keltner Channels.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> kc_data = market.technical.kc(data=stock_data.results, length=20, scalar=20, mamode='ema', offset=0)
        >>> market.technical.kc(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/kc",
            **filter_inputs(
                data=data,
                index=index,
                length=length,
                scalar=scalar,
                mamode=mamode,
                offset=offset,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def macd(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        fast: int = 12,
        slow: int = 26,
        signal: int = 9,
        chart: Annotated[
            bool,
            DataMartCustomParameter(
                description="Whether to create a chart or not, by default False."
            ),
        ] = False,
    ) -> OBBject:
        """Calculate the Moving Average Convergence Divergence (MACD).

        Difference between two Exponential Moving Averages. The Signal line is an
        Exponential Moving Average of the MACD.

        The MACD signals trend changes and indicates the start of new trend direction.
        High values indicate overbought conditions, low values indicate oversold conditions.
        Divergence with the price indicates an end to the current trend, especially if the
        MACD is at extreme high or low values. When the MACD line crosses above the
        signal line a buy signal is generated. When the MACD crosses below the signal line a
        sell signal is generated. To confirm the signal, the MACD should be above zero for a buy,
        and below zero for a sell.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        target : str
            Target column name.
        fast : int, optional
            Number of periods for the fast EMA, by default 12.
        slow : int, optional
            Number of periods for the slow EMA, by default 26.
        signal : int, optional
            Number of periods for the signal EMA, by default 9.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Moving Average Convergence Divergence (MACD).
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> macd_data = market.technical.macd(data=stock_data.results, target='close', fast=12, slow=26, signal=9)
        >>> # Example with mock data.
        >>> market.technical.macd(fast=2, slow=3, signal=1, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/macd",
            **filter_inputs(
                data=data,
                target=target,
                index=index,
                fast=fast,
                slow=slow,
                signal=signal,
                chart=chart,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def obv(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        offset: int = 0,
    ) -> OBBject:
        """Calculate the On Balance Volume (OBV).

        Is a cumulative total of the up and down volume. When the close is higher than the
        previous close, the volume is added to the running total, and when the close is
        lower than the previous close, the volume is subtracted from the running total.

        To interpret the OBV, look for the OBV to move with the price or precede price moves.
        If the price moves before the OBV, then it is a non-confirmed move. A series of rising peaks,
        or falling troughs, in the OBV indicates a strong trend. If the OBV is flat, then the market
        is not trending.

        Parameters
        ----------
        data : List[Data]
            List of data to apply the indicator to.
        index : str, optional
            Index column name, by default "date"
        offset : int, optional
            How many periods to offset the result, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            List of data with the indicator applied.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the On Balance Volume (OBV).
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> obv_data = market.technical.obv(data=stock_data.results, offset=0)
        >>> market.technical.obv(data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/obv",
            **filter_inputs(
                data=data,
                index=index,
                offset=offset,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def rsi(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 14,
        scalar: float = 100.0,
        drift: int = 1,
        chart: Annotated[
            bool,
            DataMartCustomParameter(
                description="Whether to create a chart or not, by default False."
            ),
        ] = False,
    ) -> OBBject:
        """Calculate the Relative Strength Index (RSI).

        RSI calculates a ratio of the recent upward price movements to the absolute price
        movement. The RSI ranges from 0 to 100.
        The RSI is interpreted as an overbought/oversold indicator when
        the value is over 70/below 30. You can also look for divergence with price. If
        the price is making new highs/lows, and the RSI is not, it indicates a reversal.

        Parameters
        ----------
        data : List[Data]
            The data to use for the RSI calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date"
        length : int, optional
            The length of the RSI, by default 14
        scalar : float, optional
            The scalar to use for the RSI, by default 100.0
        drift : int, optional
            The drift to use for the RSI, by default 1

        Returns
        -------
        OBBject[List[Data]]
            The RSI data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Relative Strength Index (RSI).
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> rsi_data = market.technical.rsi(data=stock_data.results, target='close', length=14, scalar=100.0, drift=1)
        >>> market.technical.rsi(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/rsi",
            **filter_inputs(
                data=data,
                target=target,
                index=index,
                length=length,
                scalar=scalar,
                drift=drift,
                chart=chart,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def sma(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 50,
        offset: int = 0,
        chart: Annotated[
            bool,
            DataMartCustomParameter(
                description="Whether to create a chart or not, by default False."
            ),
        ] = False,
    ) -> OBBject:
        """Calculate the Simple Moving Average (SMA).

        Moving Averages are used to smooth the data in an array to
        help eliminate noise and identify trends. The Simple Moving Average is literally
        the simplest form of a moving average. Each output value is the average of the
        previous n values. In a Simple Moving Average, each value in the time period carries
        equal weight, and values outside of the time period are not included in the average.
        This makes it less responsive to recent changes in the data, which can be useful for
        filtering out those changes.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            Number of periods to be used for the calculation, by default 50.
        offset : int, optional
            Offset from the current period, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Chande Momentum Oscillator.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> sma_data = market.technical.sma(data=stock_data.results, target='close', length=50, offset=0)
        >>> market.technical.sma(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/sma",
            **filter_inputs(
                data=data,
                target=target,
                index=index,
                length=length,
                offset=offset,
                chart=chart,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def stoch(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        fast_k_period: Annotated[int, Ge(ge=0)] = 14,
        slow_d_period: Annotated[int, Ge(ge=0)] = 3,
        slow_k_period: Annotated[int, Ge(ge=0)] = 3,
    ) -> OBBject:
        """Calculate the Stochastic Oscillator.

        The Stochastic Oscillator measures where the close is in relation
        to the recent trading range. The values range from zero to 100. %D values over 75
        indicate an overbought condition; values under 25 indicate an oversold condition.
        When the Fast %D crosses above the Slow %D, it is a buy signal; when it crosses
        below, it is a sell signal. The Raw %K is generally considered too erratic to use
        for crossover signals.

        Parameters
        ----------
        data : List[Data]
            The data to use for the Stochastic Oscillator calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        fast_k_period : NonNegativeInt, optional
            The fast %K period, by default 14.
        slow_d_period : NonNegativeInt, optional
            The slow %D period, by default 3.
        slow_k_period : NonNegativeInt, optional
            The slow %K period, by default 3.

        Returns
        -------
        OBBject[List[Data]]
            The Stochastic Oscillator data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Stochastic Oscillator.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> stoch_data = market.technical.stoch(data=stock_data.results, fast_k_period=14, slow_d_period=3, slow_k_period=3)
        """  # noqa: E501

        return self._run(
            "/technical/stoch",
            **filter_inputs(
                data=data,
                index=index,
                fast_k_period=fast_k_period,
                slow_d_period=slow_d_period,
                slow_k_period=slow_k_period,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def vwap(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        anchor: str = "D",
        offset: int = 0,
    ) -> OBBject:
        """Calculate the Volume Weighted Average Price (VWAP).

        Measures the average typical price by volume.
        It is typically used with intraday charts to identify general direction.
        It helps to understand the true average price factoring in the volume of transactions,
        and serves as a benchmark for assessing the market's direction over short periods, such as a single trading day.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        anchor : str, optional
            Anchor period to use for the calculation, by default "D".
            See Timeseries Offset Aliases below for additional options:
            https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases
        offset : int, optional
            Offset from the current period, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Volume Weighted Average Price (VWAP).
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> vwap_data = market.technical.vwap(data=stock_data.results, anchor='D', offset=0)
        >>> market.technical.vwap(data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/vwap",
            **filter_inputs(
                data=data,
                index=index,
                anchor=anchor,
                offset=offset,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def wma(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 50,
        offset: int = 0,
        chart: Annotated[
            bool,
            DataMartCustomParameter(
                description="Whether to create a chart or not, by default False."
            ),
        ] = False,
    ) -> OBBject:
        """Calculate the Weighted Moving Average (WMA).

        A Weighted Moving Average puts more weight on recent data and less on past data.
        This is done by multiplying each bar's price by a weighting factor. Because of its
        unique calculation, WMA will follow prices more closely than a corresponding Simple
        Moving Average.

        Parameters
        ----------
        data : List[Data]
            The data to use for the calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            The length of the WMA, by default 50.
        offset : int, optional
            The offset of the WMA, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The WMA data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Average True Range (ATR).
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> wma_data = market.technical.wma(data=stock_data.results, target='close', length=50, offset=0)
        >>> market.technical.wma(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/wma",
            **filter_inputs(
                data=data,
                target=target,
                index=index,
                length=length,
                offset=offset,
                chart=chart,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def zlma(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 50,
        offset: int = 0,
        chart: Annotated[
            bool,
            DataMartCustomParameter(
                description="Whether to create a chart or not, by default False."
            ),
        ] = False,
    ) -> OBBject:
        """Calculate the zero lag exponential moving average (ZLEMA).

        Created by John Ehlers and Ric Way. The idea is do a
        regular exponential moving average (EMA) calculation but
        on a de-lagged data instead of doing it on the regular data.
        Data is de-lagged by removing the data from "lag" days ago
        thus removing (or attempting to) the cumulative effect of
        the moving average.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            Number of periods to be used for the calculation, by default 50.
        offset : int, optional
            Offset to be used for the calculation, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the Chande Momentum Oscillator.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp')
        >>> zlma_data = market.technical.zlma(data=stock_data.results, target='close', length=50, offset=0)
        >>> market.technical.zlma(length=2, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/technical/zlma",
            **filter_inputs(
                data=data,
                target=target,
                index=index,
                length=length,
                offset=offset,
                chart=chart,
                data_processing=True,
            )
        )
