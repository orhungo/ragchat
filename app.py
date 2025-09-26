import os
from dotenv import load_dotenv
from azure_services.llm import get_llm
from azure_services.retriever import get_retriever
from azure_services.rag_chain import get_rag_chain

load_dotenv()

def main():
    llm = get_llm()
    retriever = get_retriever()
    qa_chain = get_rag_chain(llm, retriever)

    print("🚀 RAG Chatbot hazır. Çıkmak için 'exit' yaz.")
    while True:
        query = input("\nKullanıcı: ")
        if query.lower() in ["exit", "quit", "q"]:
            print("Çıkış yapılıyor...")
            break

        result = qa_chain.invoke({"query": query})

        print("\n🤖 Bot:", result["result"])
        print("📚 Kaynaklar:")
        for doc in result["source_documents"]:
            print("-", doc.metadata.get("source", "bilinmiyor"))

if __name__ == "__main__":
    main()