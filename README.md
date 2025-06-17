# MiniMCP: Example code for MCP-enabled LLM agents

Code examples used in workshops to teach essential concepts of working with
Model Context Protocol (MCP) and LLMs agents.

Throughout the examples, we'll be using: 

- [FastMCP](https://github.com/jlowin/fastmcp) for ...
- [LangChain](https://www.langchain.com/) to connect the MCP server's capabilities (tools, resources, ...) to LLMs
- [LangGraph](https://www.langchain.com/langgraph) to build agents that use the MCP server's capabilities to fulfill tasks

# Example 1: Mini MCP client & server

## Files

- minimcp_client.py
- minimcp_server.py

## Concepts

- How to write a MCP server with multiple capabilities (tools and resources)
- How to connect to the server with a client
- How to access the server's capabilities
- Understand modes: Client and server can be used in stdio (local) and sse mode (http)

## Setup

### 1. Install Dependencies

```sh
uv add fastmcp
```

## Usage

### 2. Start the Server

#### Stdio Mode (default)
```sh
uv run minimcp-server.py
```

#### SSE Mode (HTTP)
```sh
uv run minimcp-server.py --mode sse
```

Your server will be reachable at: http://127.0.0.1:8000/sse

### 3. Run the Client

#### Stdio Mode (default)
```sh
python minimcp-client.py
```

The client will create its own server using minimcp-server.py, so that you do 
NOT need to run minimcp-server.py in stdio mode for local testing.

#### SSE Mode (HTTP)
```sh
python minimcp-client.py --serverpath http://127.0.0.1:8000/sse
```

# Example 2: Scan capabilities

## Files

- scan_capabilities.py
- pretty_capabilties.py

## Concepts

- How to access any server's capabilities
- How to get human-readable information about the server's capabilities

## Setup

### Install Dependencies

```sh
uv add fastmcp
uv add langgraph
```

## Usage

List the capabilities of any MCP server (if it does not require authentication).

```
uv run scan_capabilities.py --serverpath <PATH>
```

Some servers to try out:

- https://mcp.deepwiki.com/mcp

Alternative, you can test locally via stdio mode using

```sh
uv run scan_capabilities.py
```

This will use minimcp_server.py to create its own server.

Or you can test locally via sse mode using

```sh
uv run minimcp_server.py --mode sse &
uv run scan_capabilities.py --serverpath http://127.0.0.1:8000/sse
```

Then either reuse the server in the next examples or kill it.

# Example 3: Equip a ReAct agent with an MCP server's tools 

## Files

- toolchat.py

## Concepts

- How to bind MCP tools to a LLM 
- How to make an agent fulfill tasks using the tools

## Setup

### Install Dependencies

```sh
uv add fastmcp
uv add langgraph
uv add langchain-ollama
```

### Have Ollama available

This example requires you to have ollama with llama3.1 running.

## Usage

Launch the agent with all tools from any MCP server (if it does not require
authentication).

```sh
uv run toolchat.py --serverpath <PATH>
```

This will load all tools from the MCP server at <PATH> and make them available
to the agent.

You will the be asked for a prompt in the terminal. When you hit enter, the
agent will start processing your prompt and will call the tools from the MCP
server if it sees fit.

Of course, you can again use minimcp_server.py for local testing, using either
sse or stdio mode.
