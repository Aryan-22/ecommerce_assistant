import os
from langchain_astradb import AstraDBVectorStore
from typing import List
from langchain_core.documents import Document
from utils.config_loader import load_config
from utils.model_loader import ModelLoader
from dotenv import load_dotenv

class Retriever:
    def __init__(self):
        """_summary_
        """
        pass

    def _load_env_variables(self):
        """_summary_
        """
        pass

    def load_retriever(self):
        """_summary_
        """
        pass

    def call_retriever(self,user_query:str, top_k:int=3)
        """_summary_
        """
        pass

if __name__ == "__main__":
    retriever_obj = Retriever()
    user_query = "what is the capital of India?"
    results = retriever_obj.call_retriever(user_query)
    for idx,doc in enumerate(results,1):
        print(f"Result {idx}: {doc.page_content}\nMetadata: {doc.metadata}\n")
        