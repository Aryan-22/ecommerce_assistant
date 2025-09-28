import os
from langchain_astradb import AstraDBVectorStore
from typing import List
from langchain_core.documents import Document
from utils.config_loader import load_config
from utils.model_loader import ModelLoader
from dotenv import load_dotenv
from langchain.retrievers.document_compressors import LLMChainFilter
from langchain.retrievers import ContextualCompressionRetriever
class Retriever:
    def __init__(self):
        """_summary_
        """
        self.model_loader = ModelLoader()
        self.config = load_config()
        self._load_env_variables()
        self.vstore = None
        self.retriever = None

    def _load_env_variables(self):
        """
        Load and validate required environment variables.
        """
        load_dotenv()
        
        required_vars = ["GOOGLE_API_KEY", "ASTRA_DB_API_ENDPOINT", "ASTRA_DB_APPLICATION_TOKEN", "ASTRA_DB_KEYSPACE"]
        
        missing_vars = [var for var in required_vars if os.getenv(var) is None]
        if missing_vars:
            raise EnvironmentError(f"Missing environment variables: {missing_vars}")

    def load_retriever(self):
        """_summary_
        """
        if not self.vstore:
            collection_name = self.config["astra_db"]["collection_name"]
            self.vstore = AstraDBVectorStore(
                embedding= self.model_loader.load_embeddings(),
                collection_name=collection_name,
                api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"),
                token=os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
                namespace=os.getenv("ASTRA_DB_KEYSPACE"),
            )
        if not self.retriever:
            top_k = self.config["retriever"]["top_k"] if "retriever" in self.config else 3
            mmr_retriever = self.vstore.as_retriever(search_type="mmr", search_kwargs={"k": top_k,"fetch_k":20,"lambda_ult":0.5,"score_threshold":0.3})
            print("Retriever loaded successfully.")
            llm = self.model_loader.load_llm()
            compressor = LLMChainFilter.from_llm(llm)
            self.retriever = ContextualCompressionRetriever(base_compressor=compressor,base_retriever=mmr_retriever)
            return self.retriever

    def call_retriever(self,user_query:str):
        """_summary_
        """
        retriever = self.load_retriever()
        output = retriever.invoke(user_query)
        return output
if __name__ == "__main__":
    retriever_obj = Retriever()
    user_query = "what is the capital of India?"
    results = retriever_obj.call_retriever(user_query)
    for idx,doc in enumerate(results,1):
        print(f"Result {idx}: {doc.page_content}\nMetadata: {doc.metadata}\n")
