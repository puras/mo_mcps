from datetime import datetime

from fastmcp import FastMCP

mcp = FastMCP("MCP工具-日期时间")

@mcp.tool(name="当前时间")
def current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=5100)