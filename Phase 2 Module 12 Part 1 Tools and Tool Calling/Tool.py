from langchain_core.tools import tool

@tool
def greet(name:str)->str:
    """
    Greet a user by name. 
    """
    return f"Hello {name}"

print(greet.invoke({"name":"Nishan"}))