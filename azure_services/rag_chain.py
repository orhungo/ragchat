from langchain.chains import RetrievalQA

def get_rag_chain(llm, retriever):
    """
    LLM ve retriever kullanarak RAG chain oluşturur.
    """
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True, 
        chain_type="stuff"             
    )