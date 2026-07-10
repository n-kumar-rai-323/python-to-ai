from langchain_core.prompts import PromptTemplate
translate_prompt = PromptTemplate.from_template(
    """
    Translate the following text into {language}.
    Text:
    {text}
    """
    
)