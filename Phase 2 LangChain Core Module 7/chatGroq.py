from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=1000,
    timeout=30,
    max_retries=2
)
response = llm.invoke("Explain AI.")
print(response.content)