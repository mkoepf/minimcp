import argparse
import asyncio
from fastmcp import Client
from langchain_mcp_adapters.resources import load_mcp_resources
from langchain_mcp_adapters.tools import load_mcp_tools
from pretty_capabilities import pretty_print_capabilities


async def main(path_to_server: str):
    """
    Main entry point for running the toolchat agent.

    Connects to a MCP server and prints a list of tools and resources.

    Args:
        path_to_server (str, optional): Path to the MCP server.
    """
    async with Client(path_to_server) as client:

        # Load tools from the MCP server
        try:
            tools = await load_mcp_tools(client.session)
        except Exception as e:
            print(f"Failed to load tools: {e}")
            tools = []

        # Load resources from the MCP server
        try:
            resources = await load_mcp_resources(client.session)
        except Exception as e:
            print(f"Failed to load resources: {e}")
            resources = []

        # Pretty print the loaded tools and resources
        pretty_print_capabilities(tools, resources)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the toolchat agent.")
    parser.add_argument(
        "--serverpath",
        type=str,
        default="minimcp_server.py",
        help="Path to the tool server script (default: minimcp_server.py, "
        "i.e. stdio mode).",
    )
    args = parser.parse_args()

    asyncio.run(main(args.serverpath))
