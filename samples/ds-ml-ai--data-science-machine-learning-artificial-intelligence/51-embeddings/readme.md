

*   https://medium.com/biased-algorithms/word-embeddings-in-python-a8085488d244


*   models

    *   Word2Vec
    
    *   GloVe
    
    *   FastText

*   https://docs.langchain.com/oss/python/integrations/text_embedding

    Similarity metrics
Several metrics are commonly used to compare embeddings:
Cosine similarity — measures the angle between two vectors.
Euclidean distance — measures the straight-line distance between points.
Dot product — measures how much one vector projects onto another.

```python
import numpy as np

def cosine_similarity(vec1, vec2):
    dot = np.dot(vec1, vec2)
    return dot / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

similarity = cosine_similarity(query_embedding, document_embedding)
print("Cosine Similarity:", similarity)
```


Interface
LangChain provides a standard interface for text embedding models (e.g., OpenAI, Cohere, Hugging Face) via the Embeddings interface.
Two main methods are available:
embed_documents(texts: List[str]) → List[List[float]]: Embeds a list of documents.
embed_query(text: str) → List[float]: Embeds a single query.


Model	Package
OpenAIEmbeddings	langchain-openai
AzureOpenAIEmbeddings	langchain-openai
GoogleGenerativeAIEmbeddings	langchain-google-genai
OllamaEmbeddings	langchain-ollama
TogetherEmbeddings	langchain-together
FireworksEmbeddings	langchain-fireworks
MistralAIEmbeddings	langchain-mistralai
CohereEmbeddings	langchain-cohere
NomicEmbeddings	langchain-nomic
FakeEmbeddings	langchain-core
DatabricksEmbeddings	databricks-langchain
WatsonxEmbeddings	langchain-ibm
NVIDIAEmbeddings	langchain-nvidia
AimlapiEmbeddings	langchain-aimlapi


```python
import time
from langchain_classic.embeddings import CacheBackedEmbeddings  
from langchain_classic.storage import LocalFileStore 
from langchain_core.vectorstores import InMemoryVectorStore

# Create your underlying embeddings model
underlying_embeddings = ... # e.g., OpenAIEmbeddings(), HuggingFaceEmbeddings(), etc.

# Store persists embeddings to the local filesystem
# This isn't for production use, but is useful for local
store = LocalFileStore("./cache/") 

cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings,
    store,
    namespace=underlying_embeddings.model
)

# Example: caching a query embedding
tic = time.time()
print(cached_embedder.embed_query("Hello, world!"))
print(f"First call took: {time.time() - tic:.2f} seconds")

# Subsequent calls use the cache
tic = time.time()
print(cached_embedder.embed_query("Hello, world!"))
print(f"Second call took: {time.time() - tic:.2f} seconds")
```