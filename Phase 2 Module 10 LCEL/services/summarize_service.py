from chains.study_chains import summarize_chain

class SummarizeService:
    @staticmethod
    def summarize(text: str)->str:
        response = summarize_chain.invoke(
            {
                "text":text,
            },
            config={
                "tags":[
                    "study-ai",
                    "summarize",
                ],
                "metadata":{
                    "feature":"summarize"
                }
            }
        )
        return str(response.content)