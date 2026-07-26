from mcp.server.fastmcp import FastMCP, Context
import hashlib

EMAIL = "23f2004186@ds.study.iitm.ac.in"

mcp = FastMCP("exam")


@mcp.tool()
async def solve_challenge(ctx: Context) -> str:
    request = ctx.request
    challenge = request.headers.get("X-Exam-Challenge", "")

    return hashlib.sha256(
        f"{challenge}:{EMAIL}".encode()
    ).hexdigest()[:16]


app = mcp.streamable_http_app()
