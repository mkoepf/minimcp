import argparse
import asyncio

from fastmcp import Client
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_mcp_adapters.resources import load_mcp_resources, Blob
from langchain_mcp_adapters.tools import BaseTool, load_mcp_tools
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from typing import Any

from pretty_capabilities import pretty_print_tools


def init_llm():
    """
    Initialize and return a ChatOllama language model with preset parameters.

    Returns:
        ChatOllama: The initialized language model.
    """
    return ChatOllama(
        model="llama3.1",
        temperature=0.7,
        num_predict=1000,
    )


async def run_agent(
    llm: BaseChatModel, tools: list[BaseTool], msg: str
) -> Any:
    """
    Run the agent with the given language model, tools, and input message.

    Args:
        llm (BaseChatModel): The language model to use.
        tools (list[BaseTool]): The tools available to the agent.
        msg (str): The message to process.

    Returns:
        Any: The result of the agent's processing.
    """
    agent = create_react_agent(llm, tools)
    return await agent.ainvoke(
        {"messages": msg},
    )


async def main(path_to_server: str = "minimcp_server.py"):
    """
    Main entry point for running the toolchat agent.

    Connects to the MCP server, loads tools and resources, and runs the agent.

    Args:
        path_to_server (str, optional): Path to the tool server script.
        Defaults to "minimcp_server.py".
    """
    async with Client(path_to_server) as client:

        # Load tools from the MCP server
        try:
            tools = await load_mcp_tools(client.session)
        except Exception as e:
            print(f"Failed to load tools: {e}")
            tools = []

        # Pretty print the loaded tools and resources
        pretty_print_tools(tools)

        # Run the agent with the loaded tools (TODO: and resources)
        llm: BaseChatModel = init_llm()
        inp = input("Enter a prompt for the agent: ")
        result = await run_agent(llm, tools, inp)
        print(f"Result: {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the toolchat agent.")
    parser.add_argument(
        "--serverpath",
        type=str,
        default="minimcp_server.py",
        help="Path to the tool server script (default: minimcp_server.py), "
        "i.e. stdio mode.",
    )
    args = parser.parse_args()

    asyncio.run(main(args.serverpath))
