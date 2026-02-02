from mcp.server.fastmcp import Context, FastMCP
from mcp.types import TextContent

# Create the server
mcp = FastMCP("example-streaming-server")


@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
