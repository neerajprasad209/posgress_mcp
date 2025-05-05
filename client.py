# client.py
import os
import asyncio
from google import genai                             # Gemini client :contentReference[oaicite:14]{index=14}
from google.genai import types
from mcp import ClientSession, StdioServerParameters # MCP session & stdio transport :contentReference[oaicite:15]{index=15}
from mcp.client.stdio import stdio_client

from dotenv import load_dotenv
import os

load_dotenv() 

async def main():
    # Initialize Gemini
    client = genai.Client(api_key="AIzaSyBmZ1V57IqyV3TTUWvyXdTjhEjHoH-Nosg")

    # Configure FastMCP server process
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
        env={"PG_CONN": os.getenv("PG_CONN")},
    )

    # Start MCP server and Gemini session
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()      # Handshake: discover tools :contentReference[oaicite:16]{index=16}

            # List available tools and convert to Gemini function specs
            mcp_tools = await session.list_tools()
            functions = []
            for tool in mcp_tools.tools:
                functions.append(
                    types.Tool(
                        function_declarations=[{
                            "name": tool.name,
                            "description": tool.description,
                            "parameters": {
                                k: v for k, v in tool.inputSchema.items()
                                if k not in ["additionalProperties", "$schema"]
                            },
                        }]
                    )
                )

            # Example prompt: count users in region 'North'
            prompt = "Get the number of users per country in the users table."
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0,
                    tools=functions,
                ),
            )

            # After receiving the response from generate_content
            function_calls = response.function_calls
            # Check if there are any function calls
            if function_calls:
                # Access the first function call
                function_call = function_calls[0]
                
                # Proceed to call the tool with the function name and arguments
                result = await session.call_tool(
                    function_call.name,
                    arguments=dict(function_call.args),
                )
                
                # Print the result
                print("Query Result:", result)
            else:
                print("No function calls were returned in the response.")

if __name__ == "__main__":
    asyncio.run(main())
