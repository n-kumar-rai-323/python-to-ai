from langchain_core.prompts import PromptTemplate

summarize_prompt = PromptTemplate.from_template(
    """
    Summarize the following text.
    Text:
    {text}
    """
)