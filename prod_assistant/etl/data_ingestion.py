import os
import pandas as pd
from dotenv import load_dotenv
from typing import List
from langchain_core.documents import Document
from langchain_astradb import AstraDBVectorStore
from prod_assistant.utils.model_loader import ModelLoader
from prod_assistant.utils.config_loader import load_config


class DataIngestion:
    """
    Class to handle data ingestion from CSV files and store them in AstraDB.
    """
    def __init__(self):
        """
        _summary_
        """
        pass

    def _load_env_variables(self):
        """
        load environment variables from .env file.
        """
        pass

    def get_csv_path(self):
        """
        get the path of the csv file.
        """
        pass

    def _load_csv(self):
        """
        load the csv file and return a pandas dataframe.
        """

    def transform_data(self):
        """
        
        transform the data for ingestion.
        """
        pass
    def store_in_vector_db(self):
        """
        store the transformed data in AstraDB.
        """
        pass
    
    def run_pipeline(self):
        """
        run the entire data ingestion pipeline.
        """
        pass