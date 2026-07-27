from collections.abc import Iterable


class StreamingService:
    def __init__(self, agent):
        self.agent = agent

    def stream_messages(self, question: str, thread_id: str) -> Iterable[str]:
        for chunk in self.agent.stream(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question,
                    }
                ]
            },
            config={
                "configurable": {
                    "thread_id": thread_id
                }
            },
            stream_mode="messages",
        ):
            token, metadata = chunk

            if token.text:
                yield token.text