from fastapi import APIRouter
from app.schemas.query import QueryRequest, QueryResponse # Import the request and response schemas
from app.services.query_service import answer_question

router = APIRouter() # Create a router for the query endpoint

# Define the query endpoint
@router.post("/query", response_model=QueryResponse)

# Handle the query request
def query(request: QueryRequest):
    # Answer the question
    answer = answer_question(request.question)
    # Return the answer
    return QueryResponse(answer=answer)