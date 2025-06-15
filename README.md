# MiniMCP Example: Server & Client

Minimal FastMCP server and client setup for sharing 
a resource using the Model Context Protocol (MCP).

Used in workshops to teach essential MCP concepts.

## Features
- **Server**: Serves a resource at `file://resource.txt` via FastMCP.
- **Client**: Connects to the server and retrieves the resource content.
- **Modes**: Both server and client support `stdio` (default, local) and `sse` (HTTP) modes.

---

## Setup

### 1. Install Dependencies
Make sure you have [fastmcp](https://pypi.org/project/fastmcp/) installed.

---

## Usage

### 2. Start the Server

#### Stdio Mode (default)
```sh
python minimcp-server.py
```

#### SSE Mode (HTTP)
```sh
python minimcp-server.py --mode sse
```

---

### 3. Run the Client

#### Stdio Mode (default)
```sh
python minimcp-client.py
```

The client will create its own server using minimcp-server.py, so that you do 
NOT need to run minimcp-server.py in stdio mode for local testing.

#### SSE Mode (HTTP)
```sh
python minimcp-client.py --mode sse
```

---

## How It Works
- The server provides a resource at `file://resource.txt`.
- The client requests this resource and prints its content.
- Both scripts use argparse to select the mode (`stdio` or `sse`).

---
