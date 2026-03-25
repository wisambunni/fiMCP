from typing import Any
from constants import ALPHA_VANTAGE_FUNCTIONS
from shared.shared import alpha_vantage_client
import sys
import tools.indicators # register mcp tools
from shared.shared import mcp

from utils.utils import truncate_indicator_first_n

@mcp.tool()
async def get_price(symbol: str) -> dict[str, Any] | None:
    '''Get latest stock price

    Args:
        symbol: Stock symbol
    '''
    try:
        prices = await alpha_vantage_client.make_request(ALPHA_VANTAGE_FUNCTIONS.TIME_SERIES_DAILY, symbol=symbol)
        return prices
    except Exception as e:
        return {"error": f"Error fetching price for {symbol}: {str(e)}"}


if __name__ == '__main__':
    try:
        mcp.run()
    except Exception as e:
        print('...', file=sys.stderr)
