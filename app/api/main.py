from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.query import router as query_router

# Create the FastAPI application
app = FastAPI(
    title="AI Knowledge Assistant API",
    version="1.0.0"
)

# API routes  
app.include_router(health_router) # Include the health check router
app.include_router(query_router) # Include the query router