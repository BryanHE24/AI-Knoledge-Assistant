from app.query.query_pipeline import run_query
from app.core.exceptions import KnowledgeBaseUnavailable

# query service class to handle queries using the RAG pipeline
class QueryService:
    def answer_question(self, question: str) -> str:
        """Answer a question using the RAG pipeline"""
        answer = run_query(question)

        # Check if the answer indicates the knowledge base is unavailable
        if "don't have access to my knowledge base" in answer.lower():
            raise KnowledgeBaseUnavailable()

        return answer