from langchain_core.prompts import ChatPromptTemplate

translate_prompt= ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a professional translator.
            Rules:
            - Preserve the original meaning.
            - Use natural language.
            - Do not add extra explanations. 
            """
        ),(
            "human",
            """
            Translate the following text into {language}.
            Text:
            {text} 
            """
        )
    ]
)