from fastmcp import FastMCP
from typing import Any
import argparse

mcp: FastMCP[Any] = FastMCP("MCP demo server")


@mcp.tool
def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.
    """
    return a + b + 5


@mcp.tool
def zipzap(degree: int) -> str:
    """
    Solves the famous zipzap problem to an arbitrary degree.
    """
    return "zop" * degree


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
