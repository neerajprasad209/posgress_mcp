# server.py
import os
import json
import psycopg2
from fastmcp import FastMCP  # High-level MCP framework :contentReference[oaicite:8]{index=8}

# Initialize FastMCP server
mcp = FastMCP(name="PostgresMCP")

@mcp.tool(name="query_postgres", description="Run a read-only SQL query returning JSON")
def query_postgres(sql: str) -> str:
    """
    Execute a SQL query in a read-only transaction and return results as JSON.
    """
    conn = psycopg2.connect(os.getenv("PG_CONN"))      # e.g. "postgresql://user:pass@host:port/db"
    cur = conn.cursor()
    # Enforce read-only
    cur.execute("BEGIN TRANSACTION READ ONLY;")
    cur.execute(sql)
    rows = cur.fetchall()
    # Optional: retrieve column names for better JSON output
    cols = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    # Return JSON string
    return json.dumps([dict(zip(cols, row)) for row in rows])

if __name__ == "__main__":
    # Start server over stdio (default transport) :contentReference[oaicite:9]{index=9}
    mcp.run(transport="stdio")
