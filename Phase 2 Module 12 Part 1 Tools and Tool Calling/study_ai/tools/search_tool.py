from langchain_core.tools import tool
@tool
def search_tool(query:str)->str:
    """
    Search information from the internet.
    """
    return f"Search result for: {query}"