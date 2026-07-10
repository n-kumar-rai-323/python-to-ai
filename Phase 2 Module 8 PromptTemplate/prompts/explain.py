from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate.from_template(
    """
    You are an export teacher.
    Explain the following topic in simple language.
    Topic:
    {topic}
    """
    
)