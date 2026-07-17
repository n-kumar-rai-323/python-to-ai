from chains.study_chains import explain_chain

class ExplainService:
    @staticmethod
    def explain(topic: str)->str:
        response = explain_chain.invoke(
            {
                "topic":topic,
            },
            config={
                "tags":[
                    "study-ai",
                    "explain",
                ],
                "metadata":{
                    "feature":"explain"
                }
            }
        )
        print("============",response)
        print("============",response.response_metadata)
        print("============",response.usage_metadata)

        return str(response.content)