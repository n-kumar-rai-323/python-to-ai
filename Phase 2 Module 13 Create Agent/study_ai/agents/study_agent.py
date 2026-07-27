from langgraph.prebuilt import create_react_agent
from study_ai.config.llm import llm
from study_ai.tools import (calculator_tool, search_tool, weather_tool)
agent = create_react_agent(
    model=llm,
    tools=[
        weather_tool, calculator_tool, search_tool
    ],
)