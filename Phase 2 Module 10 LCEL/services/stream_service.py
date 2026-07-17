from collections.abc import Iterator

from langchain_core.messages import AIMessage
from chains.study_chains import explain_chain

class StreamService:
    @staticmethod
    def stream_explanation(topic:str)-> Iterator[AIMessage]:
        for chunk in explain_chain.stream(
            {
                "topic":topic
            },
            config={
                "tags":[
                    "study-ai",
                    "stream"
                ],
                "metadata":{
                    "feature":"stream_explanation"
                }
            }
        ):
            yield chunk