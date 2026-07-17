from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

explain_prompt =ChatPromptTemplate.from_messages(
    [
        ("system","""
         You are an expert AI teacher.
         Your responsibility is to teach beginner students.
         Rules:
         - Explain step by step
         - Use simple language.
         - explain why before how.
         - Include a practical example.
         - Keep the explanation technically correct.
         """),(
             "human",
             """ 
             Explain the following topic:
             {topic}
             """
         )
    ]
)