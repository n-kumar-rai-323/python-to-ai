from langgraph.checkpoint.postgres import PostgresSaver
from study_ai.agents.study_agent import build_agent
from study_ai.config.database import DATABASE_URL

THREAD_ID="user-001"


def chat(agent):
    while True:
        question=input("\nYou : ")
        if question.lower()=="exit":
            break
        response = agent.invoke(
            {
                "messages":[
                    {
                        "role":"user",
                        "content":question
                    }
                ]
            },
            config={
                "configurable":{
                    "thread_id":THREAD_ID
                }
            },
        )
        print()
        print("AI : ",response["messages"][-1].content)
def main():
    with PostgresSaver.from_conn_string(DATABASE_URL) as checkpointer:
        checkpointer.setup()
        agent = build_agent(checkpointer)
        chat(agent)
if __name__ == "__main__":
    main()
