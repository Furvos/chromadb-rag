import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(
    name="direito_constitucional",
    embedding_function=DefaultEmbeddingFunction(),
    configuration={
        "hnsw": {
            "space": "cosine",
            "max_neighbors": 16,
            "ef_construction": 200,
        }
    }
)