from typing import Any
from mcp.server.fastmcp import FastMCP
from retriever.retrieval import Retriever
from langchain_community.tools import DuckDuckGoSearchRun

mcp = FastMCP("hybrid_search")

retriever_obj = Retriever()
retriever = retriever_obj.load_retriever()

duckduckgo = DuckDuckGoSearchRun()

#---------Helpers---------
def _format_docs(self, docs) -> str:
    '''Format retrieved documents for better readability.'''

    if not docs:
        return "No relevant documents found."
    formatted_chunks = []
    for d in docs:
        meta = d.metadata or {}
        formatted = (
            f"Title: {meta.get('product_title', 'N/A')}\n"
            f"Price: {meta.get('price', 'N/A')}\n"
            f"Rating: {meta.get('rating', 'N/A')}\n"
            f"Reviews:\n{d.page_content.strip()}"
        )
        formatted_chunks.append(formatted)
    return "\n\n---\n\n".join(formatted_chunks)

#retrieved_contexts = [_format_docs(retrieved_docs)]

#---------MCP Tools---------
@mcp.tool()
async def get_product_info(query: str) -> str:

    """
    Retrieve product information from the vector database.
    """
    try:
        docs = retriever.invoke(query)
        context = _format_docs(retriever_obj, docs)
        if not context.strip():
            return "No relevant documents found."
        return context
    
    except Exception as e:
        return f"Error retrieving product info: {str(e)}"
    

@mcp.tool()
async def web_search(query: str) -> str:
    """
    Perform a web search using DuckDuckGo search if retriever is not available.
    """
    try:
        result = duckduckgo.run(query)
        return result if result else "No data from web"
    except Exception as e:
        return f"Error performing web search: {str(e)}"
if __name__ == "__main__":
    mcp.run(transport = "stdio")
