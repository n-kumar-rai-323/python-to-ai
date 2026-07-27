from langchain_core.tools import tool

@tool
def weather_tool(city: str) -> str:
    """
    Get the current weather of a city.
    """
    weather_data = {
        "kathmandu": "28°C, Cloudy",
        "pokhara": "16°C, Sunny",
        "delhi": "38°C, Hot",
    }

    return weather_data.get(
        city.lower(),
        "Weather not available"
    )