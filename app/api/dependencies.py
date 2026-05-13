from app.services.query_service import QueryService

# Dependency function to get the query service
def get_query_service() -> QueryService:
    return QueryService()