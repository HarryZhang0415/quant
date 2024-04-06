from datetime import date

import pytest
from datamart_core.app.service.user_service import UserService
from datamart_yfinance.models.active import YFActiveFetcher
from datamart_yfinance.models.aggressive_small_caps import YFAggressiveSmallCapsFetcher
from datamart_yfinance.models.available_indices import YFinanceAvailableIndicesFetcher
from datamart_yfinance.models.balance_sheet import YFinanceBalanceSheetFetcher
from datamart_yfinance.models.cash_flow import YFinanceCashFlowStatementFetcher
from datamart_yfinance.models.company_news import YFinanceCompanyNewsFetcher
from datamart_yfinance.models.crypto_historical import YFinanceCryptoHistoricalFetcher
from datamart_yfinance.models.currency_historical import YFinanceCurrencyHistoricalFetcher
from datamart_yfinance.models.equity_historical import YFinanceEquityHistoricalFetcher
from datamart_yfinance.models.equity_profile import YFinanceEquityProfileFetcher
from datamart_yfinance.models.equity_quote import YFinanceEquityQuoteFetcher
from datamart_yfinance.models.etf_historical import YFinanceEtfHistoricalFetcher
from datamart_yfinance.models.etf_info import YFinanceEtfInfoFetcher
from datamart_yfinance.models.futures_curve import YFinanceFuturesCurveFetcher
from datamart_yfinance.models.futures_historical import YFinanceFuturesHistoricalFetcher
from datamart_yfinance.models.gainers import YFGainersFetcher
from datamart_yfinance.models.growth_tech_equities import YFGrowthTechEquitiesFetcher
from datamart_yfinance.models.historical_dividends import (
    YFinanceHistoricalDividendsFetcher,
)
from datamart_yfinance.models.income_statement import YFinanceIncomeStatementFetcher
from datamart_yfinance.models.index_historical import (
    YFinanceIndexHistoricalFetcher,
)
from datamart_yfinance.models.key_executives import YFinanceKeyExecutivesFetcher
from datamart_yfinance.models.key_metrics import YFinanceKeyMetricsFetcher
from datamart_yfinance.models.losers import YFLosersFetcher
from datamart_yfinance.models.market_indices import (
    YFinanceMarketIndicesFetcher,
)
from datamart_yfinance.models.price_target_consensus import (
    YFinancePriceTargetConsensusFetcher,
)
from datamart_yfinance.models.share_statistics import YFinanceShareStatisticsFetcher
from datamart_yfinance.models.undervalued_growth_equities import (
    YFUndervaluedGrowthEquitiesFetcher,
)
from datamart_yfinance.models.undervalued_large_caps import YFUndervaluedLargeCapsFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [
            ("User-Agent", None),
            ("Cookie", "MOCK_COOKIE"),
            ("crumb", "MOCK_CRUMB"),
        ],
        "filter_query_parameters": [
            ("period1", "MOCK_PERIOD_1"),
            ("period2", "MOCK_PERIOD_2"),
            ("crumb", "MOCK_CRUMB"),
        ],
    }


@pytest.mark.record_http
def test_y_finance_crypto_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "BTCUSD",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
        "interval": "1d",
    }

    fetcher = YFinanceCryptoHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_currency_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "EURUSD",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
    }

    fetcher = YFinanceCurrencyHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_index_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "^GSPC",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
    }

    fetcher = YFinanceIndexHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_equity_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "AAPL",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
        "interval": "1d",
    }

    fetcher = YFinanceEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_historical_dividends_fetcher(credentials=test_credentials):
    params = {"symbol": "IBM"}

    fetcher = YFinanceHistoricalDividendsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_market_indices_fetcher(credentials=test_credentials):
    params = {
        "symbol": "^GSPC",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
    }

    fetcher = YFinanceMarketIndicesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_futures_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "ES=F",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
    }

    fetcher = YFinanceFuturesHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.skip("Unreliable amount of data while recording test.")
@pytest.mark.record_http
def test_y_finance_futures_curve_fetcher(credentials=test_credentials):
    params = {"symbol": "ES"}

    fetcher = YFinanceFuturesCurveFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_company_news_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL,MSFT"}

    fetcher = YFinanceCompanyNewsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_balance_sheet_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceBalanceSheetFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_cash_flow_statement_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceCashFlowStatementFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_income_statement_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceIncomeStatementFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


def test_y_finance_available_fetcher(credentials=test_credentials):
    params = {}

    fetcher = YFinanceAvailableIndicesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_etf_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SPY",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = YFinanceEtfHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_active_fetcher(credentials=test_credentials):
    params = {}

    fetcher = YFActiveFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_gainers_fetcher(credentials=test_credentials):
    params = {}

    fetcher = YFGainersFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_losers_fetcher(credentials=test_credentials):
    params = {}

    fetcher = YFLosersFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_undervalued_large_caps_fetcher(credentials=test_credentials):
    params = {}

    fetcher = YFUndervaluedLargeCapsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_undervalued_growth_equities_fetcher(credentials=test_credentials):
    params = {}

    fetcher = YFUndervaluedGrowthEquitiesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_aggressive_small_caps_fetcher(credentials=test_credentials):
    params = {}

    fetcher = YFAggressiveSmallCapsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_growth_tech_equities_fetcher(credentials=test_credentials):
    params = {}

    fetcher = YFGrowthTechEquitiesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_equity_profile_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceEquityProfileFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_equity_quote_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceEquityQuoteFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_price_target_consensus_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinancePriceTargetConsensusFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_share_statistics_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceShareStatisticsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_key_executives_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceKeyExecutivesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_key_metrics_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceKeyMetricsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_etf_info_fetcher(credentials=test_credentials):
    params = {"symbol": "QQQ"}

    fetcher = YFinanceEtfInfoFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
