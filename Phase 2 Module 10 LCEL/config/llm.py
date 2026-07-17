from langchain_groq import ChatGroq

from config.settings import GROQ_API_KEY
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=1000,
    timeout=30,
    max_retries=2
)