from langchain_core.tools import tool

@tool
def calculator_tool(number1:float, number2:float, operation:str)->str:
    """
    Mathematical calculator.
    """
    if operation == "add":
        return str(number1 + number1)
    if operation == "subtract":
        return str(number1 - number2)
    if operation == "multiply":
        return str(number1 * number2)
    if operation == "divide":
        if number2 ==0:
            return "Cannot divide by zero."
        return str(number1 / number2)
    return "Invalid operation."