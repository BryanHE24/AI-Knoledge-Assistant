from typing import List
from openai import OpenAI
from app.core.config import settings

# OpenAI embedder class
class OpenAIEmbedder:
    # initialize the OpenAI embedder
    def __init__(self, model: str = None):
        self.client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url=settings.OPENROUTER_BASE_URL
        )
        self.model = model or settings.OPENROUTER_MODEL

    # embed texts using batching
    def embed_texts(self, texts: List[str], batch_size: int = 20) -> List[List[float]]:
        """
        Embed texts using batching.
        """
        all_embeddings = []
        # iterate over texts in batches
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]

            # create embeddings for the batch
            response = self.client.embeddings.create(
                model=self.model,
                input=batch
            )

            # extract embeddings from response
            batch_embeddings = [item.embedding for item in response.data]
            all_embeddings.extend(batch_embeddings)

        return all_embeddings