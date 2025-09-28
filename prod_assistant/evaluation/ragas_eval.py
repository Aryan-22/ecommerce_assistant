from ragas import SingleTurnSample
from utils.model_loader import ModelLoader
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.metrics import LLMContextPrecisionWithoutReference,ResponseRelevancy
import grpc.experimental.aio as grpc_aio
import asyncio

grpc_aio.init_grpc_aio()
model_loader = ModelLoader()


def evaluate_context_precision(query,response,retrieved_context):
    """
    __summary__
        Evaluate context precision without reference using LLMContextPrecisionWithoutReference metric.
    """
    try:
        sample = SingleTurnSample(
            user_input = query,
            response = response,
            retrieved_contexts=retrieved_context,
        )
        async def main():
            llm = model_loader.load_llm()
            evaluator_llm = LangchainLLMWrapper(llm)
            context_precision = LLMContextPrecisionWithoutReference(llm = evaluator_llm)
            result = await context_precision.single_turn_ascore(sample)
            return result

        return asyncio.run(main())
    except Exception as e:
        return e

def evaluate_response_relevancy(query,response,retrieved_context):
    """
    __summary__
        Evaluate response relevancy using ResponseRelevancy metric.
    """
    try:
        sample = SingleTurnSample(
            user_input = query,
            response=response,
            retrieved_contexts=retrieved_context,
        )
        async def main():
            llm = model_loader.load_llm()
            embeddings = model_loader.load_embeddings()
            evaluator_llm = LangchainLLMWrapper(llm)
            evaluator_embeddings = LangchainEmbeddingsWrapper(embeddings)
            response_relevancy = ResponseRelevancy(llm = evaluator_llm,embeddings=evaluator_embeddings)
            result = await response_relevancy.single_turn_ascore(sample)
            return result

        return asyncio.run(main())
    except Exception as e:
        return e

    

