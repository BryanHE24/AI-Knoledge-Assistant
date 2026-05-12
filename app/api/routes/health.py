from fastapi import APIRouter
from app.schemas.health import HealthResponse # Import the health response schema
router = APIRouter() # Create a router for the health check endpoint

# Health check endpoint
@router.get("/health", response_model=HealthResponse)  
def health_check():
    return HealthResponse(status="ok") # Return the status of the API