from langchain_core.prompts import (ChatPromptTemplate)

summarize_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert document summarizer.
            
            Rules:
            - Extract the important information.
            - Remove unnecessary repetion.
            - Keep technical meaning accurate.
            - Return a concise summary.
            """
        ),(
            "human",
            """
            Summarize the following text:
            {text} 
            """
        )
    ]
)