from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.query import router as query_router
from app.api.exception_handlers import knowledge_base_exception_handler
from app.core.exceptions import KnowledgeBaseUnavailable
from app.api.middleware import request_logging_middleware

# Create the FastAPI application
app = FastAPI(
    title="AI Knowledge Assistant API",
    version="1.0.0"
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

# Middleware
app.middleware("http")(request_logging_middleware) # Add the request logging middleware

# Exception handlers
app.add_exception_handler(
    KnowledgeBaseUnavailable, knowledge_base_exception_handler  
)