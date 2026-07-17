from chains.study_chains import explain_chain


class BatchService:
    @staticmethod
    def batch_explain(topics:list[str])->list[str]:
        inputs =[
            {
                "topic":topic,
            }
            for topic in topics
        ]
        responses =explain_chain.batch(
            inputs,
            config={
                "tags":[
                    "study-ai",
                    "batch"
                ],
                "metadata":{
                    "feature":"batch_explain",
                },
                "max_concurrency":3
            }
        )
        return [
            str(response.content)
            for response in responses
        ]