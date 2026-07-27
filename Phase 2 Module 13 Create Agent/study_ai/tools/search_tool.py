from langchain_core.tools import tool
@tool
def search_tool(query:str)->str:
    """
    Search latest information.
    """
    return f"Search Result:{query}"
    