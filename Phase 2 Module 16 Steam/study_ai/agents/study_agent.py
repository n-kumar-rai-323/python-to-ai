from langchain.agents import create_agent

from study_ai.config.llm import llm
from study_ai.tools import (
    weather_tool,
    calculator_tool,
    search_tool,
)


def build_agent(checkpointer):

    agent = create_agent(
        model=llm,
        tools=[
            weather_tool,
            calculator_tool,
            search_tool,
        ],
        checkpointer=checkpointer,
        system_prompt="You are a helpful AI study assistant."
    )

    return agent