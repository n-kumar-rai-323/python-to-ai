from study_ai.agents import agent

THREAD_ID="user-001"
def chat():
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
if __name__ == "__main__":
    chat()
