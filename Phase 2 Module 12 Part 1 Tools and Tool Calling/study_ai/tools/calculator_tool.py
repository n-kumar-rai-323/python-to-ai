from langchain_core.tools import tool
@tool
def calculator_tool(number1:float, number2:float,operation:str)->str:
    """
    Perform mathematical calculations.
    Supported operations:
    add
    subtract
    multiply
    divide
    """
    if operation =="add":
        return str(number1 + number2)
    elif operation == "subtract":
        return str(number1 - number2)
    elif operation =="multiply":
        return str(number1 * number2)
    elif operation == "divide":
        if number2 ==0:
            return "cannot divide by zero."
        return str(number1 / number2)
    return "Invalid operation."