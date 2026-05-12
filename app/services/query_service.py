from app.query.query_pipeline import run_query

# Service function to answer a question
def answer_question(question: str) -> str:
    """Answer a question using the RAG pipeline"""
    return run_query(question)