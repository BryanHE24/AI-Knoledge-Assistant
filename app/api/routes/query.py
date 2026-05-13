from fastapi import APIRouter, Depends
from app.schemas.query import QueryRequest, QueryResponse
from app.services.query_service import QueryService
from app.api.dependencies import get_query_service

router = APIRouter() # Create a router for the query endpoint

# Define the query endpoint
@router.post("/query", response_model=QueryResponse)

# Handle the query request
def query(
    request: QueryRequest,
    query_service: QueryService = Depends(get_query_service)
):
    # Answer the question
    answer = query_service.answer_question(request.question)
    # Return the answer
    return QueryResponse(answer=answer)