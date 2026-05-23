from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.query import router as query_router
from app.api.exception_handlers import knowledge_base_exception_handler
from app.core.exceptions import KnowledgeBaseUnavailable
from fastapi.middleware.cors import CORSMiddleware

from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from app.core.rate_limiter import limiter

# Create the FastAPI application
app = FastAPI(
    title="AI Knowledge Assistant API",
    version="1.0.0"
)

# Rate limiting middleware
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


# API routes
# Include the health check router
app.include_router(
    health_router,
    prefix="/api/v1"
)

# Include the query router
app.include_router(
    query_router,
    prefix="/api/v1"
)

# Exception handlers
app.add_exception_handler(
    KnowledgeBaseUnavailable, knowledge_base_exception_handler  
)