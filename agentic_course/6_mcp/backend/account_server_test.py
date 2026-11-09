from mcp.server.fastmcp import FastMCP
from accounts import Account

mcp = FastMCP("account_servers")

@mcp.tool()
async def get_balance(name: str) -> None:
    """
    Get the cash balance of the given account name
    Args:
        name (str): account name
    """
    return Account.get(name).balance


if __name__ == "__main__":
    mcp.run(transport="stdio")