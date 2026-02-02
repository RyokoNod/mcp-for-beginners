import logging

import mcp.types as types
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("mcp_client")


class LoggingCollector:
    def __init__(self):
        self.log_messages: list[types.LoggingMessageNotificationParams] = []

    async def __call__(self, params: types.LoggingMessageNotificationParams) -> None:
        self.log_messages.append(params)
        logger.info("MCP Log: %s - %s", params.level, params.data)


logging_collector = LoggingCollector()
port = 8000


async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)


async def run():
    async with streamablehttp_client(f"http://localhost:{port}/mcp") as (
        read_stream,
        write_stream,
        session_callback,
    ):
        async with ClientSession(
            read_stream,
            write_stream,
            logging_callback=logging_collector,
            message_handler=message_handler,
        ) as session:
            id_before = session_callback()
            logger.info("Session ID before init: %s", id_before)
            await session.initialize()
            id_after = session_callback()
            logger.info("Session ID after init: %s", id_after)
            logger.info("Session initialized, ready to call tools.")
            tool_result = await session.call_tool(
                "process_files", {"message": "hello from client"}
            )
            logger.info("Tool result: %s", tool_result)
            if logging_collector.log_messages:
                logger.info("Collected log messages:")
                for log in logging_collector.log_messages:
                    logger.info("Log: %s", log)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
