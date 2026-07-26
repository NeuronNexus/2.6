from mcp.server.fastmcp import FastMCP
from starlette.requests import Request
import hashlib

EMAIL = "23f2004186@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("exam-server")


@mcp.tool()
async def solve_challenge(request: Request) -> str:
    challenge = request.headers.get("X-Exam-Challenge", "")

    digest = hashlib.sha256(
        f"{challenge}:{EMAIL}".encode()
    ).hexdigest()

    return digest[:16]


app = mcp.streamable_http_app()