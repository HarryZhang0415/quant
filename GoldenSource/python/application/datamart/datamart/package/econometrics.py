### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from datamart_core.app.static.container import Container
from datamart_core.app.model.obbject import OBBject
import pandas
import numpy
from typing import List, Union, Literal
from annotated_types import Gt
from typing_extensions import Annotated
from datamart_core.app.static.utils.decorators import exception_handler, validate

from datamart_core.app.static.utils.filters import filter_inputs

from datamart_core.provider.abstract.data import Data


class ROUTER_econometrics(Container):
    """/econometrics
    autocorrelation
    causality
    cointegration
    correlation_matrix
    ols_regression
    ols_regression_summary
    panel_between
    panel_first_difference
    panel_fixed
    panel_fmac
    panel_pooled
    panel_random_effects
    residual_autocorrelation
    unit_root
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def autocorrelation(
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
        y_column: str,
        x_columns: List[str],
    ) -> OBBject:
        """Perform Durbin-Watson test for autocorrelation.

        The Durbin-Watson test is a widely used method for detecting the presence of autocorrelation in the residuals
        from a statistical or econometric model. Autocorrelation occurs when past values in the data series influence
        future values, which can be a critical issue in time-series analysis, affecting the reliability of
        model predictions. The test provides a statistic that ranges from 0 to 4, where a value around 2 suggests
        no autocorrelation, values towards 0 indicate positive autocorrelation, and values towards 4 suggest
        negative autocorrelation. Understanding the degree of autocorrelation helps in refining models to better capture
        the underlying dynamics of the data, ensuring more accurate and trustworthy results.

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        y_column: str
            Target column.
        x_columns: List[str]
            List of columns to use as exogenous variables.

        Returns
        -------
        OBBject[Dict]
            OBBject with the results being the score from the test.

        Examples
        --------
        >>> from datamart import market
        >>> # Perform Durbin-Watson test for autocorrelation.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp').to_df()
        >>> market.econometrics.autocorrelation(data=stock_data, y_column="close", x_columns=["open", "high", "low"])
        >>> market.econometrics.autocorrelation(y_column='close', x_columns=['open', 'high', 'low'], data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/econometrics/autocorrelation",
            **filter_inputs(
                data=data,
                y_column=y_column,
                x_columns=x_columns,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def causality(
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
        y_column: str,
        x_column: str,
        lag: Annotated[int, Gt(gt=0)] = 3,
    ) -> OBBject:
        """Perform Granger causality test to determine if X 'causes' y.

        The Granger causality test is a statistical hypothesis test to determine if one time series is useful in
        forecasting another. While 'causality' in this context does not imply a cause-and-effect relationship in
        the philosophical sense, it does test whether changes in one variable are systematically followed by changes
        in another variable, suggesting a predictive relationship. By specifying a lag, you set the number of periods to
        look back in the time series to assess this relationship. This test is particularly useful in economic and
        financial data analysis, where understanding the lead-lag relationship between indicators can inform investment
        decisions and policy making.

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        y_column: str
            Target column.
        x_column: str
            Columns to use as exogenous variables.
        lag: PositiveInt
            Number of lags to use in the test.

        Returns
        -------
        OBBject[Data]
            OBBject with the results being the score from the test.

        Examples
        --------
        >>> from datamart import market
        >>> # Perform Granger causality test to determine if X 'causes' y.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp').to_df()
        >>> market.econometrics.causality(data=stock_data, y_column="close", x_column="open")
        >>> # Example with mock data.
        >>> market.econometrics.causality(y_column='close', x_column='open', lag=1, data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/econometrics/causality",
            **filter_inputs(
                data=data,
                y_column=y_column,
                x_column=x_column,
                lag=lag,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def cointegration(
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
        columns: List[str],
    ) -> OBBject:
        """Show co-integration between two timeseries using the two step Engle-Granger test.

        The two-step Engle-Granger test is a method designed to detect co-integration between two time series.
        Co-integration is a statistical property indicating that two or more time series move together over the long term,
        even if they are individually non-stationary. This concept is crucial in economics and finance, where identifying
        pairs or groups of assets that share a common stochastic trend can inform long-term investment strategies
        and risk management practices. The Engle-Granger test first checks for a stable, long-term relationship by
        regressing one time series on the other and then tests the residuals for stationarity.
        If the residuals are found to be stationary, it suggests that despite any short-term deviations,
        the series are bound by an equilibrium relationship over time.

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        columns: List[str]
            Data columns to check cointegration
        maxlag: PositiveInt
            Number of lags to use in the test.

        Returns
        -------
        OBBject[Data]
            OBBject with the results being the score from the test.

        Examples
        --------
        >>> from datamart import market
        >>> # Perform co-integration test between two timeseries.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp').to_df()
        >>> market.econometrics.cointegration(data=stock_data, columns=["open", "close"])
        """  # noqa: E501

        return self._run(
            "/econometrics/cointegration",
            **filter_inputs(
                data=data,
                columns=columns,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def correlation_matrix(
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
    ) -> OBBject:
        """Get the correlation matrix of an input dataset.

        The correlation matrix provides a view of how different variables in your dataset relate to one another.
        By quantifying the degree to which variables move in relation to each other, this matrix can help identify patterns,
        trends, and potential areas for deeper analysis. The correlation score ranges from -1 to 1, with -1 indicating a
        perfect negative correlation, 0 indicating no correlation, and 1 indicating a perfect positive correlation.

        Parameters
        ----------
        data : List[Data]
            Input dataset.

        Returns
        -------
        OBBject[List[Data]]
            Correlation matrix.

        Examples
        --------
        >>> from datamart import market
        >>> # Get the correlation matrix of a dataset.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp').to_df()
        >>> market.econometrics.correlation_matrix(data=stock_data)
        >>> market.econometrics.correlation_matrix(data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/econometrics/correlation_matrix",
            **filter_inputs(
                data=data,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def ols_regression(
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
        y_column: str,
        x_columns: List[str],
    ) -> OBBject:
        """Perform Ordinary Least Squares (OLS) regression.

        OLS regression is a fundamental statistical method to explore and model the relationship between a
        dependent variable and one or more independent variables. By fitting the best possible linear equation to the data,
        it helps uncover how changes in the independent variables are associated with changes in the dependent variable.
        This returns the model and results objects from statsmodels library.

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        y_column: str
            Target column.
        x_columns: List[str]
            List of columns to use as exogenous variables.

        Returns
        -------
        OBBject[Dict]
            OBBject with the results being model and results objects.

        Examples
        --------
        >>> from datamart import market
        >>> # Perform Ordinary Least Squares (OLS) regression.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp').to_df()
        >>> market.econometrics.ols_regression(data=stock_data, y_column="close", x_columns=["open", "high", "low"])
        >>> market.econometrics.ols_regression(y_column='close', x_columns=['open', 'high', 'low'], data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/econometrics/ols_regression",
            **filter_inputs(
                data=data,
                y_column=y_column,
                x_columns=x_columns,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def ols_regression_summary(
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
        y_column: str,
        x_columns: List[str],
    ) -> OBBject:
        """Perform Ordinary Least Squares (OLS) regression.

        This returns the summary object from statsmodels.

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        y_column: str
            Target column.
        x_columns: List[str]
            List of columns to use as exogenous variables.

        Returns
        -------
        OBBject[Data]
            OBBject with the results being summary object.

        Examples
        --------
        >>> from datamart import market
        >>> # Perform Ordinary Least Squares (OLS) regression and return the summary.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp').to_df()
        >>> market.econometrics.ols_regression_summary(data=stock_data, y_column="close", x_columns=["open", "high", "low"])
        >>> market.econometrics.ols_regression_summary(y_column='close', x_columns=['open', 'high', 'low'], data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/econometrics/ols_regression_summary",
            **filter_inputs(
                data=data,
                y_column=y_column,
                x_columns=x_columns,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def panel_between(
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
        y_column: str,
        x_columns: List[str],
    ) -> OBBject:
        """Perform a Between estimator regression on panel data.

        The Between estimator for regression analysis on panel data is focusing on the differences between entities
        (such as individuals, companies, or countries) over time. By aggregating the data for each entity and analyzing the
        average outcomes, this method provides insights into the overall impact of explanatory variables (x_columns) on
        the dependent variable (y_column) across all entities.

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        y_column: str
            Target column.
        x_columns: List[str]
            List of columns to use as exogenous variables.

        Returns
        -------
        OBBject[Dict]
            OBBject with the fit model returned

        Examples
        --------
        >>> from datamart import market
        >>> market.econometrics.panel_between(y_column='portfolio_value', x_columns=['risk_free_rate'], data=[{'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_1', 'time': 0, 'portfolio_value': 100000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_1', 'time': 1, 'portfolio_value': 150000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_2', 'time': 0, 'portfolio_value': 150000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_2', 'time': 1, 'portfolio_value': 133333.33, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_3', 'time': 0, 'portfolio_value': 133333.33, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_3', 'time': 1, 'portfolio_value': 125000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_4', 'time': 0, 'portfolio_value': 125000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_4', 'time': 1, 'portfolio_value': 120000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_5', 'time': 0, 'portfolio_value': 120000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_5', 'time': 1, 'portfolio_value': 116666.67, 'risk_free_rate': 0.02}])
        """  # noqa: E501

        return self._run(
            "/econometrics/panel_between",
            **filter_inputs(
                data=data,
                y_column=y_column,
                x_columns=x_columns,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def panel_first_difference(
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
        y_column: str,
        x_columns: List[str],
    ) -> OBBject:
        """Perform a first-difference estimate for panel data.

        The First-Difference estimator for panel data analysis is focusing on the changes between consecutive observations
        for each entity (such as individuals, companies, or countries). By differencing the data, this method effectively
        removes entity-specific effects that are constant over time, allowing for the examination of the impact of changes
        in explanatory variables (x_columns) on the change in the dependent variable (y_column).

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        y_column: str
            Target column.
        x_columns: List[str]
            List of columns to use as exogenous variables.

        Returns
        -------
        OBBject[Dict]
            OBBject with the fit model returned

        Examples
        --------
        >>> from datamart import market
        >>> market.econometrics.panel_first_difference(y_column='portfolio_value', x_columns=['risk_free_rate'], data=[{'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_1', 'time': 0, 'portfolio_value': 100000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_1', 'time': 1, 'portfolio_value': 150000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_2', 'time': 0, 'portfolio_value': 150000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_2', 'time': 1, 'portfolio_value': 133333.33, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_3', 'time': 0, 'portfolio_value': 133333.33, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_3', 'time': 1, 'portfolio_value': 125000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_4', 'time': 0, 'portfolio_value': 125000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_4', 'time': 1, 'portfolio_value': 120000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_5', 'time': 0, 'portfolio_value': 120000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_5', 'time': 1, 'portfolio_value': 116666.67, 'risk_free_rate': 0.02}])
        """  # noqa: E501

        return self._run(
            "/econometrics/panel_first_difference",
            **filter_inputs(
                data=data,
                y_column=y_column,
                x_columns=x_columns,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def panel_fixed(
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
        y_column: str,
        x_columns: List[str],
    ) -> OBBject:
        """One- and two-way fixed effects estimator for panel data.

        The Fixed Effects estimator to panel data is enabling a focused analysis on the unique characteristics of entities
        (such as individuals, companies, or countries) and/or time periods. By controlling for entity-specific and/or
        time-specific influences, this method isolates the effect of explanatory variables (x_columns) on the dependent
        variable (y_column), under the assumption that these entity or time effects capture unobserved heterogeneity.

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        y_column: str
            Target column.
        x_columns: List[str]
            List of columns to use as exogenous variables.

        Returns
        -------
        OBBject[Dict]
            OBBject with the fit model returned

        Examples
        --------
        >>> from datamart import market
        >>> market.econometrics.panel_fixed(y_column='portfolio_value', x_columns=['risk_free_rate'], data=[{'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_1', 'time': 0, 'portfolio_value': 100000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_1', 'time': 1, 'portfolio_value': 150000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_2', 'time': 0, 'portfolio_value': 150000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_2', 'time': 1, 'portfolio_value': 133333.33, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_3', 'time': 0, 'portfolio_value': 133333.33, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_3', 'time': 1, 'portfolio_value': 125000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_4', 'time': 0, 'portfolio_value': 125000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_4', 'time': 1, 'portfolio_value': 120000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_5', 'time': 0, 'portfolio_value': 120000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_5', 'time': 1, 'portfolio_value': 116666.67, 'risk_free_rate': 0.02}])
        """  # noqa: E501

        return self._run(
            "/econometrics/panel_fixed",
            **filter_inputs(
                data=data,
                y_column=y_column,
                x_columns=x_columns,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def panel_fmac(
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
        y_column: str,
        x_columns: List[str],
    ) -> OBBject:
        """Fama-MacBeth estimator for panel data.

        The Fama-MacBeth estimator, a two-step procedure renowned for its application in finance to estimate the risk
        premiums and evaluate the capital asset pricing model. By first estimating cross-sectional regressions for each
        time period and then averaging the regression coefficients over time, this method provides insights into the
        relationship between the dependent variable (y_column) and explanatory variables (x_columns) across different
        entities (such as individuals, companies, or countries).

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        y_column: str
            Target column.
        x_columns: List[str]
            List of columns to use as exogenous variables.

        Returns
        -------
        OBBject[Dict]
            OBBject with the fit model returned

        Examples
        --------
        >>> from datamart import market
        >>> market.econometrics.panel_fmac(y_column='portfolio_value', x_columns=['risk_free_rate'], data=[{'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_1', 'time': 0, 'portfolio_value': 100000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_1', 'time': 1, 'portfolio_value': 150000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_2', 'time': 0, 'portfolio_value': 150000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_2', 'time': 1, 'portfolio_value': 133333.33, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_3', 'time': 0, 'portfolio_value': 133333.33, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_3', 'time': 1, 'portfolio_value': 125000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_4', 'time': 0, 'portfolio_value': 125000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_4', 'time': 1, 'portfolio_value': 120000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_5', 'time': 0, 'portfolio_value': 120000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_5', 'time': 1, 'portfolio_value': 116666.67, 'risk_free_rate': 0.02}])
        """  # noqa: E501

        return self._run(
            "/econometrics/panel_fmac",
            **filter_inputs(
                data=data,
                y_column=y_column,
                x_columns=x_columns,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def panel_pooled(
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
        y_column: str,
        x_columns: List[str],
    ) -> OBBject:
        """Perform a Pooled coefficient estimator regression on panel data.

        The Pooled coefficient estimator for regression analysis on panel data is treating the data as a large
        cross-section without distinguishing between variations across time or entities
        (such as individuals, companies, or countries). By assuming that the explanatory variables (x_columns) have a
        uniform effect on the dependent variable (y_column) across all entities and time periods, this method simplifies
        the analysis and provides a generalized view of the relationships within the data.

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        y_column: str
            Target column.
        x_columns: List[str]
            List of columns to use as exogenous variables.

        Returns
        -------
        OBBject[Dict]
            OBBject with the fit model returned

        Examples
        --------
        >>> from datamart import market
        >>> market.econometrics.panel_pooled(y_column='portfolio_value', x_columns=['risk_free_rate'], data=[{'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_1', 'time': 0, 'portfolio_value': 100000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_1', 'time': 1, 'portfolio_value': 150000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_2', 'time': 0, 'portfolio_value': 150000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_2', 'time': 1, 'portfolio_value': 133333.33, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_3', 'time': 0, 'portfolio_value': 133333.33, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_3', 'time': 1, 'portfolio_value': 125000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_4', 'time': 0, 'portfolio_value': 125000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_4', 'time': 1, 'portfolio_value': 120000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_5', 'time': 0, 'portfolio_value': 120000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_5', 'time': 1, 'portfolio_value': 116666.67, 'risk_free_rate': 0.02}])
        """  # noqa: E501

        return self._run(
            "/econometrics/panel_pooled",
            **filter_inputs(
                data=data,
                y_column=y_column,
                x_columns=x_columns,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def panel_random_effects(
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
        y_column: str,
        x_columns: List[str],
    ) -> OBBject:
        """Perform One-way Random Effects model for panel data.

        One-way Random Effects model to panel data is offering a nuanced approach to analyzing data that spans across both
        time and entities (such as individuals, companies, countries, etc.). By acknowledging and modeling the random
        variation that exists within these entities, this method provides insights into the general patterns that
        emerge across the dataset.

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        y_column: str
            Target column.
        x_columns: List[str]
            List of columns to use as exogenous variables.

        Returns
        -------
        OBBject[Dict]
            OBBject with the fit model returned

        Examples
        --------
        >>> from datamart import market
        >>> market.econometrics.panel_random_effects(y_column='portfolio_value', x_columns=['risk_free_rate'], data=[{'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_1', 'time': 0, 'portfolio_value': 100000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_1', 'time': 1, 'portfolio_value': 150000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_2', 'time': 0, 'portfolio_value': 150000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_2', 'time': 1, 'portfolio_value': 133333.33, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_3', 'time': 0, 'portfolio_value': 133333.33, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_3', 'time': 1, 'portfolio_value': 125000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_4', 'time': 0, 'portfolio_value': 125000.0, 'risk_free_rate': 0.03}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_4', 'time': 1, 'portfolio_value': 120000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_5', 'time': 0, 'portfolio_value': 120000.0, 'risk_free_rate': 0.02}, {'is_multiindex': True, 'multiindex_names': "['asset_manager', 'time']", 'asset_manager': 'asset_manager_5', 'time': 1, 'portfolio_value': 116666.67, 'risk_free_rate': 0.02}])
        """  # noqa: E501

        return self._run(
            "/econometrics/panel_random_effects",
            **filter_inputs(
                data=data,
                y_column=y_column,
                x_columns=x_columns,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def residual_autocorrelation(
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
        y_column: str,
        x_columns: List[str],
        lags: Annotated[int, Gt(gt=0)] = 1,
    ) -> OBBject:
        """Perform Breusch-Godfrey Lagrange Multiplier tests for residual autocorrelation.

        The Breusch-Godfrey Lagrange Multiplier test is a sophisticated tool for uncovering autocorrelation within the
        residuals of a regression model. Autocorrelation in residuals can indicate that a model fails to capture some
        aspect of the underlying data structure, possibly leading to biased or inefficient estimates.
        By specifying the number of lags, you can control the depth of the test to check for autocorrelation,
        allowing for a tailored analysis that matches the specific characteristics of your data.
        This test is particularly valuable in econometrics and time-series analysis, where understanding the independence
        of errors is crucial for model validity.

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        y_column: str
            Target column.
        x_columns: List[str]
            List of columns to use as exogenous variables.
        lags: PositiveInt
            Number of lags to use in the test.

        Returns
        -------
        OBBject[Data]
            OBBject with the results being the score from the test.

        Examples
        --------
        >>> from datamart import market
        >>> # Perform Breusch-Godfrey Lagrange Multiplier tests for residual autocorrelation.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp').to_df()
        >>> market.econometrics.residual_autocorrelation(data=stock_data, y_column="close", x_columns=["open", "high", "low"])
        >>> market.econometrics.residual_autocorrelation(y_column='close', x_columns=['open', 'high', 'low'], data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/econometrics/residual_autocorrelation",
            **filter_inputs(
                data=data,
                y_column=y_column,
                x_columns=x_columns,
                lags=lags,
                data_processing=True,
            )
        )

    @exception_handler
    @validate(config=dict(arbitrary_types_allowed=True))
    def unit_root(
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
        column: str,
        regression: Literal["c", "ct", "ctt"] = "c",
    ) -> OBBject:
        """Perform Augmented Dickey-Fuller (ADF) unit root test.

        The ADF test is a popular method for testing the presence of a unit root in a time series.
        A unit root indicates that the series may be non-stationary, meaning its statistical properties such as mean,
        variance, and autocorrelation can change over time. The presence of a unit root suggests that the time series might
        be influenced by a random walk process, making it unpredictable and challenging for modeling and forecasting.
        The 'regression' parameter allows you to specify the model used in the test: 'c' for a constant term,
        'ct' for a constant and trend term, and 'ctt' for a constant, linear, and quadratic trend.
        This flexibility helps tailor the test to the specific characteristics of your data, providing a more accurate
        assessment of its stationarity.

        Parameters
        ----------
        data: List[Data]
            Input dataset.
        column: str
            Data columns to check unit root
        regression: Literal["c", "ct", "ctt"]
            Regression type to use in the test.  Either "c" for constant only, "ct" for constant and trend, or "ctt" for
            constant, trend, and trend-squared.

        Returns
        -------
        OBBject[Data]
            OBBject with the results being the score from the test.

        Examples
        --------
        >>> from datamart import market
        >>> # Perform Augmented Dickey-Fuller (ADF) unit root test.
        >>> stock_data = market.equity.price.historical(symbol='TSLA', start_date='2023-01-01', provider='fmp').to_df()
        >>> market.econometrics.unit_root(data=stock_data, column="close")
        >>> market.econometrics.unit_root(data=stock_data, column="close", regression="ct")
        >>> market.econometrics.unit_root(column='close', data=[{'date': '2023-01-02', 'open': 110.0, 'high': 120.0, 'low': 100.0, 'close': 115.0, 'volume': 10000.0}, {'date': '2023-01-03', 'open': 165.0, 'high': 180.0, 'low': 150.0, 'close': 172.5, 'volume': 15000.0}, {'date': '2023-01-04', 'open': 146.67, 'high': 160.0, 'low': 133.33, 'close': 153.33, 'volume': 13333.33}, {'date': '2023-01-05', 'open': 137.5, 'high': 150.0, 'low': 125.0, 'close': 143.75, 'volume': 12500.0}, {'date': '2023-01-06', 'open': 132.0, 'high': 144.0, 'low': 120.0, 'close': 138.0, 'volume': 12000.0}])
        """  # noqa: E501

        return self._run(
            "/econometrics/unit_root",
            **filter_inputs(
                data=data,
                column=column,
                regression=regression,
                data_processing=True,
            )
        )
