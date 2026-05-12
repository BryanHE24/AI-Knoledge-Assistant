from pydantic import BaseModel

# 
class QueryRequest(BaseModel): 
    """Request schema for a query"""
    question: str


class QueryResponse(BaseModel):
    """Response schema for a query"""
    answer: str