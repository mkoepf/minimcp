from fastmcp import FastMCP
from typing import Any
import argparse

mcp: FastMCP[Any] = FastMCP("Resource file provider")


@mcp.resource("file://resource.txt")
def get_resource_content() -> str:
    """
    Returns the resource content.
    """
    return "This is the content of the resource file. "


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Start the FastMCP server " "in stdio or sse mode."
    )
    parser.add_argument(
        "--mode",
        choices=["stdio", "sse"],
        default="stdio",
        help="Server mode: stdio (default) or sse",
    )
    args = parser.parse_args()
    print("Starting the FastMCP server...")
    if args.mode == "sse":
        mcp.run("sse")
    else:
        mcp.run("stdio")
