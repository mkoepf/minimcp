from typing import Any, Callable
from langchain_mcp_adapters.tools import BaseTool
from langchain_mcp_adapters.resources import Blob


def pretty_print_tools(list_of_tools: list[BaseTool]) -> None:
    """
    Pretty print a list of tools with their details.

    Args:
        list_of_tools (list[BaseTool]): The list of tools to print.
    """
    pretty_print_list("Tools: ", list_of_tools, print_elem=pretty_print_tool)


def pretty_print_resources(list_of_resources: list[Blob]) -> None:
    """
    Pretty print a list of resources with their details.

    Args:
        list_of_resources (list[Blob]): The list of resources to print.
    """
    pretty_print_list(
        "Resources: ", list_of_resources, print_elem=pretty_print_resource
    )


def pretty_print_capabilities(
    list_of_tools: list[BaseTool], list_of_resources: list[Blob]
) -> None:
    """
    Pretty print both tools and resources with their details.

    Args:
        list_of_tools (list[BaseTool]): The list of tools to print.
        list_of_resources (list[Blob]): The list of resources to print.
    """
    pretty_print_tools(list_of_tools)
    pretty_print_resources(list_of_resources)


def pretty_print_list(
    name: str, items: list[Any], print_elem: Callable[[Any], None] = print
) -> None:
    """
    Pretty print a list with a title, separator lines, and a custom print
    function.

    Args:
        name (str): The name/title to display for the list.
        items (list): The list to print.
        print_elem (Callable[[Any], None], optional): Function to print each
        element. Defaults to print.
    """
    print(f"\n===[ {name} ]===".ljust(40, "=") + "\n")
    for idx, item in enumerate(items):
        if idx > 0:
            print("-" * 40 + "\n")
        print_elem(item)
    print("=" * 40)


def pretty_print_tool(tool: BaseTool) -> None:
    """
    Pretty print a tool's details in a readable format.

    Args:
        tool (BaseTool): The tool to print.
    """
    print(f"Name: {getattr(tool, 'name', None)}")
    print(f"Description: {getattr(tool, 'description', None)}")
    print("Args schema:")
    for k, v in getattr(tool, "args_schema", {}).get("properties", {}).items():
        print(f"  - {k}: {v.get('description', '')}")
    print(f"Response format: {getattr(tool, 'response_format', None)}\n")


def pretty_print_resource(resource: Blob) -> None:
    """
    Pretty print a resource's details in a readable format.

    Args:
        resource (Blob): The resource to print.
    """
    print(f"mimetype: {resource.mimetype}")
    print(f"metadata: {resource.metadata}")
    if resource.data is not None:
        print(f"data: {resource.data[:100]}...\n")  # Print first 100 chars
    else:
        print("data: None\n")
