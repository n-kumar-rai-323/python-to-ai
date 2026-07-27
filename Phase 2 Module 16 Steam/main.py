from langgraph.checkpoint.postgres import PostgresSaver

from study_ai.agents import build_agent
from study_ai.config.database import DATABASE_URL
from study_ai.services import StreamingService

THREAD_ID="user-001"
def chat(streaming_service: StreamingService):
    while True:
        question = input("\nYou : ")
        if question.lower()=="exit":
            break
        print("\nAI : ", end="", flush=True)
        for token in streaming_service.stream_messages(
            question=question,
            thread_id=THREAD_ID
        ):
            print(token, end="", flush=True)
        print()

def main():
    with PostgresSaver.from_conn_string(DATABASE_URL)as checkpointer:
        checkpointer.setup()
        agent= build_agent(checkpointer)
        streaming_service = StreamingService(agent)
        chat(streaming_service)
if __name__=="__main__":
    main()