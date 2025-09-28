from ragas import SingleTurnSample
from utils.model_loader import ModelLoader
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.metrics import LLMContextPrecisionWithoutReference,ResponseRelevancy
import grpc.experimental.aio as grpc_aio

grpc_aio.init_grpc_aio()
model_loader = ModelLoader()


def evaluate_context_precision():
    """
    __summary__
        Evaluate context precision without reference using LLMContextPrecisionWithoutReference metric.
    """
    pass

def evaluate_response_relevancy(query):
    """
    __summary__
        Evaluate response relevancy using ResponseRelevancy metric.
    """
    pass

