from fastapi import APIRouter, Depends
from app.schemas.query import QueryRequest, QueryResponse
from app.services.query_service import QueryService
from app.api.dependencies import get_query_service

from fastapi import Request
from app.core.rate_limiter import limiter

router = APIRouter() # Create a router for the query endpoint

# Define the query endpoint
@router.post("/query", response_model=QueryResponse)
@limiter.limit("5/minute")


# Handle the query request

# 5 requests per minute per IP address
@router.post("/query", response_model=QueryResponse)
@limiter.limit("5/minute")


def query(
    request: Request,
    request_body: QueryRequest,
    query_service: QueryService = Depends(get_query_service)
):
    answer = query_service.answer_question(
        request_body.question
    )
    return QueryResponse(answer=answer)