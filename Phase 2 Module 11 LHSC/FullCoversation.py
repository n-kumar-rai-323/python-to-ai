from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
messages =[
    SystemMessage(
        content ="You are an AI teacher"
    ),
    HumanMessage(
        content="Explain Python."
    ),
    AIMessage(
        content="Python is a programming language."
    )
]
for message in messages:
    print(message)