from enum import Enum, EnumMeta
from typing import Any


ALPHA_VANTAGE_API_KEY = 'ALPHA_VANTAGE_API_KEY'
ALPHA_VANTAGE_BASE_URL = 'https://www.alphavantage.co/query'

class DirectValueMeta(EnumMeta):
    '''
    Metaclass that allows for directly getting an enum attribute.
    This avoids having to access the enums by Class.Enum.value
    '''

    def __getattribute__(self, __name: str) -> Any:
        value = super().__getattribute__(__name)
        if isinstance(value, self):
            value = value.value
        return value

class ALPHA_VANTAGE_FUNCTIONS(Enum, metaclass=DirectValueMeta):
    TIME_SERIES_DAILY_ADJUSTED = 'TIME_SERIES_DAILY_ADJUSTED'
    TIME_SERIES_DAILY = 'TIME_SERIES_DAILY'
    RSI = 'RSI'
    BBANDS = 'BBANDS'
    SMA = 'SMA'
    EMA = 'EMA'
