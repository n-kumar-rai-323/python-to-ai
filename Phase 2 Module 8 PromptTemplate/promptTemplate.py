from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
     model="llama-3.3-70b-versatile",
    temperature=0,
)
prompt = PromptTemplate.from_template(
    "Explain {topic}"
)

final_prompt= prompt.format(
    topic="LangChain"
)

response =llm.invoke(
    final_prompt
)
print(response.content)