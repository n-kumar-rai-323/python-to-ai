from langgraph.prebuilt import create_react_agent

from study_ai.config.database import checkpointer
from study_ai.config.llm import llm
from study_ai.tools import (
    weather_tool,
    calculator_tool,
    search_tool,
)
agent = create_react_agent(
    model=llm,
    tools=[
        weather_tool,
        calculator_tool,
        search_tool,
    ],
    checkpointer=checkpointer,
)