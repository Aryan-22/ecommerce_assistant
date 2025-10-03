# E-commerce Product Assistant

A sophisticated AI-powered e-commerce product recommendation system that leverages web scraping, vector databases, and advanced RAG (Retrieval Augmented Generation) workflows to provide intelligent product recommendations and customer support.

##  Features

- **Web Scraping**: Automated Flipkart product and review scraping
- **Vector Database Integration**: AstraDB for efficient similarity search
- **RAG Workflows**: Both normal and agentic RAG implementations
- **Web Interface**: Streamlit UI for data scraping and FastAPI for chat interface
- **Model Support**: Google Generative AI and Groq LLM integration
- **Evaluation Metrics**: RAGAS-based context precision and response relevancy evaluation
- **MCP Server**: Model Control Protocol server implementation

##  Architecture

```
ecommerce_assistant/
├── prod_assistant/           # Main package
│   ├── config/              # Configuration files
│   ├── etl/                 # Data extraction and ingestion
│   ├── evaluation/          # RAGAS evaluation metrics
│   ├── exception/           # Custom exception handling
│   ├── logger/              # Structured logging
│   ├── mcp_servers/         # MCP server implementation
│   ├── prompt_library/      # Prompt templates
│   ├── retriever/           # Vector retrieval logic
│   ├── router/              # API routing
│   ├── utils/               # Utility functions
│   └── workflow/            # RAG workflow implementations
├── data/                    # Scraped product data
├── static/                  # Web assets
├── templates/               # HTML templates
└── notebook/               # Jupyter notebooks
```

##  Prerequisites

- Python 3.10+
- Chrome browser (for web scraping)
- AstraDB account
- Google AI API key
- Groq API key

##  Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ecommerce_assistant
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   GROQ_API_KEY=your_groq_api_key
   ASTRA_DB_API_ENDPOINT=your_astradb_endpoint
   ASTRA_DB_APPLICATION_TOKEN=your_astradb_token
   ASTRA_DB_KEYSPACE=your_keyspace
   LLM_PROVIDER=google  # or groq
   ```

##  Quick Start

### 1. Data Scraping

Run the Streamlit app to scrape product data:

```bash
streamlit run scrapper_ui.py
```

- Enter product names or descriptions
- Configure scraping parameters (max products, review count)
- Scrape and save data to CSV
- Optionally ingest data into AstraDB vector database

### 2. Running RAG Workflows

#### Normal RAG Workflow
```python
from prod_assistant.workflow.normal_rag_workflow import invoke_chain

query = "Can you suggest good budget iPhone under 1,00,000 INR?"
contexts, response = invoke_chain(query)
print(f"Response: {response}")
```

#### Agentic RAG Workflow
```python
from prod_assistant.workflow.agentic_rag_workflow import AgenticRAG

rag_agent = AgenticRAG()
answer = rag_agent.run("What is the price of iPhone 15?")
print(f"Answer: {answer}")
```

### 3. Web Chat Interface

The project includes a complete web interface with a floating chat widget. The HTML template (`templates/index.html`) provides:
- Hero section with branding
- Floating chat icon
- Real-time chat interface
- Bootstrap styling

##  Configuration

The system is configured via `prod_assistant/config/config.yaml`:

```yaml
astra_db:
  collection_name: "ecommercedata"

embedding_model:
  provider: "google"
  model_name: "models/text-embedding-004"

retriever:
  top_k: 4

llm:
  groq:
    provider: "groq"
    model_name: "deepseek-r1-distill-llama-70b"
    temperature: 0
    max_output_tokens: 2048
  
  google:
    provider: "google"
    model_name: "gemini-2.0-flash"
    temperature: 0
    max_output_tokens: 2048
```

##  Data Pipeline

1. **Scraping** (`FlipkartScraper`): Automated product and review extraction
2. **Ingestion** (`DataIngestion`): Transform and load data into AstraDB
3. **Retrieval** (`Retriever`): MMR-based similarity search with compression
4. **Generation**: LLM-powered response generation
5. **Evaluation**: RAGAS metrics for quality assessment

##  Evaluation

The system includes comprehensive evaluation using RAGAS metrics:

```python
from prod_assistant.evaluation.ragas_eval import (
    evaluate_context_precision,
    evaluate_response_relevancy
)

context_score = evaluate_context_precision(query, response, contexts)
relevancy_score = evaluate_response_relevancy(query, response, contexts)
```

##  Logging

Structured JSON logging is implemented throughout the system:

```python
from prod_assistant.logger.custom_logger import CustomLogger

logger = CustomLogger().get_logger(__file__)
logger.info("Processing query", user_id=123, query=query)
```

##  Error Handling

Custom exception handling with detailed tracebacks:

```python
from prod_assistant.exception.custom_exception import ProductAssistantException

try:
    # Some operation
    pass
except Exception as e:
    raise ProductAssistantException("Operation failed", e)
```

##  Package Structure

- **ETL Module**: Data scraping and ingestion pipelines
- **Retriever**: Vector similarity search and document compression
- **Workflow**: RAG implementation patterns
- **Utils**: Configuration and model loading utilities
- **Evaluation**: Quality assessment tools
- **MCP Servers**: Model Control Protocol integration

##  Available Scripts

- `main.py`: Basic entry point
- `scrapper_ui.py`: Streamlit scraping interface
- `get_lib_versions.py`: Check installed package versions

---

**Built with using LangChain, Streamlit, and modern AI technologies**
