from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
# Start the MCP server so I can connect to it
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=[
        "run",
        "./03-GettingStarted/02-client/server.py",
    ],  # Change path to your server script
    env=None,  # Optional environment variables
)


# Define a coroutine - a function that can pause and resume
async def run():
    # Set up read/write streams to communicate with the server.
    # async with ensures that the connection does not close until the inner await block is done
    async with stdio_client(server_params) as (read, write):
        # Create a client session using the read/write streams. This is accessible as session
        # This allows us to call MCP tools and resources without directly typing to the server
        async with ClientSession(read, write) as session:
            # Initialize the connection. Pauses until it's finished
            await session.initialize()

            # List available resources
            resources = await session.list_resource_templates()
            print("LISTING RESOURCES")
            for resource in resources:
                print("Resource: ", resource)

            # List available tools
            tools = await session.list_tools()
            print("LISTING TOOLS")
            for tool in tools.tools:
                print("Tool: ", tool.name)

            # Read a resource
            print("READING RESOURCE")
            content, mime_type = await session.read_resource("greeting://hello")
            print(f"Content: {content}, Mime Type: {mime_type}")

            # Call a tool
            print("CALL TOOL")
            result = await session.call_tool("add", arguments={"a": 1, "b": 7})
            print(result.content)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())  # Call the run coroutine
