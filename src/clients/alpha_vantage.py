import os
from typing import Any
from urllib.parse import urlencode
from constants import ALPHA_VANTAGE_API_KEY, ALPHA_VANTAGE_BASE_URL, ALPHA_VANTAGE_FUNCTIONS
import httpx

class AlphaVantageClient:
    def __init__(self):
        self._base_url = ALPHA_VANTAGE_BASE_URL
        self._api_key = os.getenv(ALPHA_VANTAGE_API_KEY)

    async def make_request(self, function: ALPHA_VANTAGE_FUNCTIONS, **kwargs) -> dict[str, Any] | None:
        url = self.build_request(function, **kwargs)
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, timeout=30)
                response.raise_for_status()
                return response.json()
            except Exception:
                return None

    def build_request(self, function: ALPHA_VANTAGE_FUNCTIONS, **kwargs) -> str:
        params = {
            'function': function,
            'apikey': self._api_key,
            **kwargs # unpack additional parameters
        }

        query_string = urlencode(params)
        return f'{self._base_url}?{query_string}'