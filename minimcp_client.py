from fastmcp import Client
import asyncio
import argparse
from typing import Any


def init_client(mode: str) -> Client[Any]:
    if mode == "stdio":
        return Client("minimcp_server.py")
    else:
        return Client("http://localhost:8000/sse")


async def get_resource(client: Client[Any]) -> str:
    async with client:
        return await client.read_resource("file://resource.txt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Test the FastMCP server via stdio or sse."
    )
    parser.add_argument(
        "--mode",
        choices=["stdio", "sse"],
        default="stdio",
        help="Connection mode: stdio (local, runs its own server) or sse "
        "(http) . Default is 'stdio'.",
    )
    args = parser.parse_args()

    print("Testing the FastMCP server...")
    client: Client[Any] = init_client(args.mode)
    result = asyncio.run(get_resource(client))
    print(f"Resource content: {result}")
    print("Test completed.")
