#!/usr/bin/env python3
# in fastmcp version 2.14.4, you don't need asyncio or serve_stdio
from fastmcp import FastMCP

# Create a FastMCP server
mcp = FastMCP(name="Weather MCP Server", version="1.0.0")


@mcp.tool()
def get_weather(location: str) -> dict:
    """Gets current weather for a location."""
    return {"temperature": 72.5, "conditions": "Sunny", "location": location}


# Alternative approach using a class
class WeatherTools:
    @mcp.tool()
    def forecast(self, location: str, days: int = 1) -> dict:
        """Gets weather forecast for a location for the specified number of days."""
        return {
            "location": location,
            "forecast": [
                {"day": i + 1, "temperature": 70 + i, "conditions": "Partly Cloudy"}
                for i in range(days)
            ],
        }


# Register class tools
weather_tools = WeatherTools()

# Start the server
if __name__ == "__main__":
    mcp.run()  # starting the server is also different in fastmcp 2.14.4
