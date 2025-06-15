from fastmcp import Client
import asyncio
import argparse


async def test_server_locall(mode: str):
    if mode == "stdio":
        client = Client("minimcp-server.py")
    else:
        client = Client("http://localhost:8000/sse")
    async with client:
        result = await client.read_resource("file://resource.txt")
        print(f"Resource content: {result}")


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
    asyncio.run(test_server_locall(args.mode))
    print("Test completed.")
