# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "fastmcp",
# ]
# ///

from fastmcp import Client
import asyncio
import argparse
from typing import Any
from mcp.types import TextResourceContents, BlobResourceContents


async def get_resources(
    client: Client[Any],
) -> list[TextResourceContents | BlobResourceContents]:
    async with client:
        return await client.read_resource("file://resource.txt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Test the FastMCP server via stdio or sse."
    )
    parser.add_argument(
        "--serverpath",
        default="minimcp_server.py",
        type=str,
        help="Path to the MCP server (default: minimcp_server.py, i.e. "
        "stdio).",
    )
    args = parser.parse_args()

    print("Testing the FastMCP server...")
    client: Client[Any] = Client(args.serverpath)

    resource_contents = asyncio.run(get_resources(client))

    print(f"Resource contents: {resource_contents}")
    print("Test completed.")

