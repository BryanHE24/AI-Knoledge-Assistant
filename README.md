# AI Knowledge Assistant API

A production-ready Retrieval-Augmented Generation (RAG) backend exposed through scalable API endpoints.

## Features

- **Document Retrieval**: Efficient document indexing and retrieval using FAISS.
- **Semantic Search**: Fast and accurate semantic search over your data.
- **`/ask` Endpoint**: Natural language query endpoint powered by LLMs.
- **Structured Responses**: Clean, typed API responses using Pydantic.
- **Docker Deployment**: Containerized for easy deployment and scaling.

## Tech Stack

- **Language**: Python 3.12
- **Framework**: FastAPI
- **LLM Integration**: OpenRouter (OpenAI Python SDK)
- **Vector Database**: FAISS
- **Validation**: Pydantic v2
- **Containerization**: Docker

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd AI-Knowledge-Assistant-API
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables

Create a `.env` file in the root directory and add the following variables:

```ini
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=text-embedding-3-small
```

## Running Locally

To start the FastAPI server locally with auto-reload:

```bash
uvicorn app.api.main:app --host 0.0.0.0 --port 8000 --reload
```

The API documentation will be available at `http://localhost:8000/docs`.

## Docker Usage

1. Build the Docker image:
   ```bash
   docker build -t ai-knowledge-assistant-api .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 --env-file .env ai-knowledge-assistant-api
   ```

## API Endpoints

- `GET /health` - Health check endpoint.
- `POST /ask` - Submit a query and retrieve an LLM-generated response augmented with retrieved documents.

Check the Swagger UI at `/docs` for detailed schemas and interactions.

## Running Tests

Run the test suite using pytest:

```bash
pytest
```

## CI Pipeline

This project uses GitHub Actions for continuous integration. The pipeline automatically runs:
- Linting and type checking
- Unit and integration tests (via pytest)
- Docker build verification

## Project Structure

```text
.
├── app/               # Main application package
│   ├── api/           # API routers and endpoints
│   ├── core/          # Configuration and setup
│   ├── embeddings/    # Embedder integrations
│   └── models/        # Pydantic models
├── data/              # Data storage (e.g., FAISS indexes)
├── docs/              # Additional documentation
├── scripts/           # Utility scripts
├── tests/             # Pytest test suite
├── Dockerfile         # Docker configuration
├── requirements.txt   # Python dependencies
└── pytest.ini         # Pytest configuration
```