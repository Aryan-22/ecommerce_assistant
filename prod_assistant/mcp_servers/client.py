import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient(
        {
            "hybrid_search":{
                "command":"python",
                "args":[r"C:\Users\aryan\ecommerce_assistant\prod_assistant\mcp_servers\product_search_server.py"
                ],
                "transport":"stdio",

            }
        }
    

    )
    tools = await client.get_tools()
    print("aAvailable tools:", [tool.name for tool in tools])
    
    #Pick tools by name
    retriever_tool = next(t for t in tools if t.name == "get_product_info")
    web_tool = next(t for t in tools if t.name == "web_search")

    #--------Try Retriever Tool--------
    query = "What is the price of iphone 14?"
    retriever_results = await retriever_tool.anvoke({"query":query})
    print("\Retriever Result:", retriever_results)
    

    #--------If retriever fails try Web search tool--------
    if not retriever_results.strip() or "No relevant product data found." in retriever_results:
        print("Retriever returned no data, trying web search...")
        web_results = await web_tool.invoke({"query":query})
        print("\nWeb Search Result:", web_results)

if __name__ == "__main__":
    asyncio.run(main())

