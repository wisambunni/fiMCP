from clients.alpha_vantage import AlphaVantageClient
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()

alpha_vantage_client = AlphaVantageClient()
mcp = FastMCP('stocks')