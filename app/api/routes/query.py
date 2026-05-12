from fastapi import APIRouter
from app.schemas.query import QueryRequest, QueryResponse # Import the request and response schemas

router = APIRouter() # Create a router for the query endpoint

# Define the query endpoint
@router.post("/query", response_model=QueryResponse) 
def query(request: QueryRequest): 
    # Return the answer
    return QueryResponse( 
        answer=f"Mock answer for: {request.question}" 
    )