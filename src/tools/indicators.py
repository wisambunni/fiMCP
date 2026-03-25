from typing import Any, Literal
from shared.shared import alpha_vantage_client, mcp
from constants import ALPHA_VANTAGE_FUNCTIONS
from utils.utils import truncate_indicator_first_n

@mcp.tool()
async def get_rsi(
    symbol: str,
    interval: Literal['1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly'] = 'weekly',
    time_period: int = 60,
    series_type: Literal['close', 'open', 'high', 'low'] = 'close'
    ) -> dict[str, Any] | None:
    '''
    Gets latest RSI level for a stock symbol over an interval

    Args:
        symbol: Stock symbol
        interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
        time_period: Number of data points used to calculate each RSI value. Positive integers are accepted (e.g., time_period=60, time_period=200)
        series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    '''
    try:
        rsi = await alpha_vantage_client.make_request(ALPHA_VANTAGE_FUNCTIONS.RSI, symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)
        return truncate_indicator_first_n(rsi)
    except Exception as e:
        return {"error": f"Error fetching RSI data for {symbol}: {str(e)}"}

@mcp.tool()
async def get_bbands(
    symbol: str,
    interval: Literal['1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly'] = 'weekly',
    time_period: int = 20,
    series_type: Literal['close', 'open', 'high', 'low'] = 'close',
    nbdevup: int = 2,
    nbdevdn: int = 2,
    matype: int = 0
    ) -> dict[str, Any] | None:
    '''
    Gets Bollinger Bands (BBANDS) for a stock symbol over an interval

    Args:
        symbol: Stock symbol
        interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
        time_period: Number of data points used to calculate each BBANDS value. Positive integers are accepted (e.g., time_period=20, time_period=200)
        series_type: The desired price type in the time series. Four types are supported: close, open, high, low
        nbdevup: The standard deviation multiplier of the upper band. Positive integers are accepted. By default, nbdevup=2
        nbdevdn: The standard deviation multiplier of the lower band. Positive integers are accepted. By default, nbdevdn=2
        matype: Type of moving average. By default, matype=0. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA)
    '''
    try:
        bbands = await alpha_vantage_client.make_request(
            ALPHA_VANTAGE_FUNCTIONS.BBANDS,
            symbol=symbol,
            interval=interval,
            time_period=time_period,
            series_type=series_type,
            nbdevup=nbdevup,
            nbdevdn=nbdevdn,
            matype=matype
        )
        return truncate_indicator_first_n(bbands)
    except Exception as e:
        return {"error": f"Error fetching Bollinger Bands data for {symbol}: {str(e)}"}

@mcp.tool()
async def get_sma(
    symbol: str,
    interval: Literal['1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly'] = 'weekly',
    time_period: int = 60,
    series_type: Literal['close', 'open', 'high', 'low'] = 'close'
    ) -> dict[str, Any] | None:
    '''
    Gets Simple Moving Average (SMA) for a stock symbol over an interval

    Args:
        symbol: Stock symbol
        interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
        time_period: Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., time_period=60, time_period=200)
        series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    '''
    try:
        sma = await alpha_vantage_client.make_request(
            ALPHA_VANTAGE_FUNCTIONS.SMA,
            symbol=symbol,
            interval=interval,
            time_period=time_period,
            series_type=series_type
        )
        return truncate_indicator_first_n(sma)
    except Exception as e:
        return {"error": f"Error fetching SMA data for {symbol}: {str(e)}"}

@mcp.tool()
async def get_ema(
    symbol: str,
    interval: Literal['1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly'] = 'weekly',
    time_period: int = 60,
    series_type: Literal['close', 'open', 'high', 'low'] = 'close'
    ) -> dict[str, Any] | None:
    '''
    Gets Exponential Moving Average (EMA) for a stock symbol over an interval

    Args:
        symbol: Stock symbol
        interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
        time_period: Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., time_period=60, time_period=200)
        series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    '''
    try:
        ema = await alpha_vantage_client.make_request(
            ALPHA_VANTAGE_FUNCTIONS.EMA,
            symbol=symbol,
            interval=interval,
            time_period=time_period,
            series_type=series_type
        )
        return truncate_indicator_first_n(ema)
    except Exception as e:
        return {"error": f"Error fetching EMA data for {symbol}: {str(e)}"}
