from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions import KnowledgeBaseUnavailable

# exception handler for knowledge base unavailable
async def knowledge_base_exception_handler(
    request: Request,
    exc: KnowledgeBaseUnavailable 
):  
    # return JSON response with 503 status code and error message
    return JSONResponse(
        status_code=503,
        content={"detail": "Knowledge base unavailable"}
    )