from langchain_groq import ChatGroq

from config.settings import GROQ_API_KEY
ll = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0,
)