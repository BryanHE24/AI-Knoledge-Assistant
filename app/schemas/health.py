from pydantic import BaseModel

# Health response schema
class HealthResponse(BaseModel): 
    status: str 