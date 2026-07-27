from langchain_core.tools import tool

@tool
def weather_tool(city:str)->str:
    """
    Get current weather of a city.
    """
    weather={
        "Kathmandu":"28C Cloudy"
    }
    return weather.get(city, "Weather not found.")