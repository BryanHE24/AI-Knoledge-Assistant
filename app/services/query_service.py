from app.query.query_pipeline import run_query

class QueryService:
    """Service class to handle queries using the RAG pipeline"""
    
    def answer_question(self, question: str) -> str:
        """Answer a question using the RAG pipeline"""
        return run_query(question)