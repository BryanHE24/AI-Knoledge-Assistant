from app.embeddings.openai_embedder import OpenAIEmbedder
from app.vectorstore.faiss_store import FAISSVectorStore


# query pipeline class
class QueryPipeline:
    # initialize the query pipeline
    def __init__(self, index_path: str):
        self.embedder = OpenAIEmbedder()

        # load FAISS index and metadata
        self.vector_store = FAISSVectorStore(dimension=1536)
        self.vector_store.load(index_path)

    # search for similar chunks
    def search(self, query: str, top_k: int = 3):
        """
        Search relevant chunks for a query.
        """

        # embed the query
        query_embedding = self.embedder.embed_texts([query])[0]

        # search for similar chunks
        results = self.vector_store.search( 
            query_embedding=query_embedding, # query embedding
            top_k=top_k # number of similar chunks to return
        )

        # return the results
        return results

def run_query(query: str) -> str:
    """
    Run a query through the RAG pipeline.
    """
    import os
    # Default index path
    index_path = os.path.join(os.getcwd(), "data", "faiss_index")
    
    # Check if index exists
    if not os.path.exists(index_path):
        return "I'm sorry, but I don't have access to my knowledge base yet. Please ensure the index is created."

    try:
        pipeline = QueryPipeline(index_path)
        results = pipeline.search(query)
        
        if not results:
            return "I couldn't find any relevant information for your question."
            
        # For now, return the best matching chunk
        # In a full RAG system, this would be passed to an LLM
        return results[0]["chunk"]["text"]
        
    except Exception as e:
        return f"An error occurred while processing your query: {str(e)}"