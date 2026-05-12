import os
from typing import List, Dict
from app.embeddings.openai_embedder import OpenAIEmbedder
from app.vectorstore.faiss_store import FAISSVectorStore

class IngestionPipeline:
    def __init__(
        self, 
        data_dir: str, 
        index_path: str, 
        chunk_size: int = 500, 
        overlap: int = 100
    ):
        self.data_dir = data_dir
        self.index_path = index_path
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.embedder = OpenAIEmbedder()
        self.vector_store = FAISSVectorStore(dimension=1536) # Default for text-embedding-3-small

    def load_documents(self) -> List[Dict]:
        """Load text documents from the data directory."""
        documents = []
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir, exist_ok=True)
            print(f"Created data directory: {self.data_dir}")
            return []

        for filename in os.listdir(self.data_dir):
            if filename.endswith(".txt"):
                path = os.path.join(self.data_dir, filename)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    documents.append({
                        "content": content,
                        "metadata": {"filename": filename}
                    })
        return documents

    def chunk_document(self, document: Dict) -> List[Dict]:
        """Chunk a single document into smaller pieces."""
        content = document["content"]
        metadata = document["metadata"]
        chunks = []
        
        start = 0
        while start < len(content):
            end = start + self.chunk_size
            chunk_text = content[start:end]
            chunks.append({
                "text": chunk_text,
                "metadata": {**metadata, "start_char": start, "end_char": end}
            })
            start += self.chunk_size - self.overlap
            
        return chunks

    def run(self):
        """Run the full ingestion pipeline."""
        print(f"Starting ingestion from {self.data_dir}...")
        
        # 1. Load documents
        documents = self.load_documents()
        if not documents:
            print("No documents found to ingest.")
            return

        print(f"Loaded {len(documents)} documents.")

        # 2. Chunk documents
        all_chunks = []
        for doc in documents:
            chunks = self.chunk_document(doc)
            all_chunks.extend(chunks)
        
        print(f"Created {len(all_chunks)} chunks.")

        # 3. Embed chunks
        texts_to_embed = [chunk["text"] for chunk in all_chunks]
        embeddings = self.embedder.embed_texts(texts_to_embed)
        
        print(f"Generated {len(embeddings)} embeddings.")

        # 4. Store in vector store
        self.vector_store.add_embeddings(embeddings, all_chunks)
        
        # 5. Save vector store
        self.vector_store.save(self.index_path)
        print(f"Saved vector index to {self.index_path}")
