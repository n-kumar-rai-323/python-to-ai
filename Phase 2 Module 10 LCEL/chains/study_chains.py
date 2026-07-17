from config.llm import llm
from prompts.explain_prompt import explain_prompt
from prompts.summarize_prompt import summarize_prompt
from prompts.translate_prompt import translate_prompt


explain_chain=(
    explain_prompt | llm
)

summarize_chain=(
    summarize_prompt | llm
)
translate_chain=( 
                 translate_prompt | llm
                 )