from fastmcp import FastMCP

mcp = FastMCP("计算器")

@mcp.tool(name="加法")
def plus(a: int, b: int) -> int:
    return a + b

@mcp.tool(name="减法")
def diff(a: int, b: int) -> int:
    return a - b

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=5200)