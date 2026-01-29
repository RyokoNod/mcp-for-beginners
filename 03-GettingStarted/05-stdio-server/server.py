# No async and asyncio needed in January 2026: FastMCP handles that internally
from mcp.server.fastmcp import FastMCP

# Create the server
mcp = FastMCP("example-stdio-server")


@mcp.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b


@mcp.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."


@mcp.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b


@mcp.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b


@mcp.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"],
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
