import os
from langchain_community.retrievers import AzureCognitiveSearchRetriever

def get_retriever():
    """
    Azure Cognitive Search retriever'ı döndürür.
    .env içindeki endpoint, api key ve index adını kullanır.
    """

    service_name = (
        os.getenv("AZURE_SEARCH_ENDPOINT")
        .replace("https://", "")
        .replace(".search.windows.net", "")
    )

    return AzureCognitiveSearchRetriever(
        service_name=service_name,
        api_key=os.getenv("AZURE_SEARCH_API_KEY"),
        index_name=os.getenv("AZURE_SEARCH_INDEX"),
        content_key="content",   
        top_k=3                 
    )