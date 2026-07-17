from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

llm = ChatGroq(
     model="llama-3.3-70b-versatile",
    temperature=0,
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
         You are an export AI teacher.
         Teach beginner students.
         Explain concepts step by step.
         Use simple examples.
         """),
        ("human", """
         Explain the following topic:
          {topic}
         """),
    ]
)

messages = prompt.invoke(
    {
        "topic":"python"
    }
)

response = llm.invoke(messages)

print(response.content)