import os
from langchain_openai import AzureChatOpenAI

def get_llm():
    """
    Azure OpenAI GPT-4o modelini döndürür.
    """
    return AzureChatOpenAI(
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        openai_api_version="2024-02-01",   
        temperature=0,
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY")
    )