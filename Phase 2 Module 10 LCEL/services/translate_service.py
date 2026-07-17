from chains.study_chains import translate_chain

class TranslateService:
    @staticmethod
    def translate(text: str, language:str)->str:
        response = translate_chain.invoke(
            {
                "text":text,
                "language":language,
            },
            config={
                "tags":[
                    "study-ai",
                    "translate",
                ],
                "metadata":{
                    "feature":"translate"
                }
            }
        )
        return str(response.content)