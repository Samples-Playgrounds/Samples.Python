# Text Transformers

*   synonyms

    *   Text Transformers

    *   Sentence Transformers

    *   Embeddings
    
        *   Vector Embeddings

Sentence Transformers SBERT

https://sbert.net/


Sentence Transformers (a.k.a. SBERT) is the go-to Python module for 

    accessing, 
    
    using, and 
    
    training 
    
state-of-the-art models

    embedding and 
    
    reranker . 
    
used 

    to compute embeddings using Sentence Transformer models 
    
        (quickstart)
        
    to calculate similarity scores using Cross-Encoder (a.k.a. reranker) models 
    
        (quickstart)
        
    to generate sparse embeddings using Sparse Encoder models 
    
        (quickstart). 
    
This unlocks a wide range of applications, including 

    semantic search, 

        https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html

    semantic textual similarity
    
        https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html

    paraphrase mining.

        https://sbert.net/examples/sentence_transformer/applications/paraphrase-mining/README.html


A wide selection of over 10,000 pre-trained Sentence Transformers models are available for immediate use on 🤗 Hugging 
Face, including many of the state-of-the-art models from the Massive Text Embeddings Benchmark (MTEB) leaderboard

    https://huggingface.co/spaces/mteb/leaderboard
    
Additionally, it is easy to train or finetune your own embedding models, reranker models, or sparse encoder models 
using Sentence Transformers, enabling you to create custom models for your specific use cases.




## Embedding AKA Sentence Transformer AKA bi-encoder Models

Characteristics of Sentence Transformer (a.k.a bi-encoder) models:

Calculates a fixed-size vector representation (embedding) given texts or images.

Embedding calculation is often efficient, embedding similarity calculation is very fast.

Applicable for a wide range of tasks, such as 

    semantic textual similarity, 
    
    semantic search, 
    
        https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html

    clustering, 
    
    classification, paraphrase mining, and more.

Often used as a first step in a two-step retrieval process, where a Cross-Encoder (a.k.a. reranker) model is used to re-rank the top-k results from the bi-encoder.


```python
from sentence_transformers import SentenceTransformer

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# The sentences to encode
sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
]

# 2. Calculate embeddings by calling model.encode()
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# 3. Calculate the embedding similarities
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.6660, 0.1046],
#         [0.6660, 1.0000, 0.1411],
#         [0.1046, 0.1411, 1.0000]])
```


## Reranker AKA Cross Encoder Models

https://sbert.net/docs/quickstart.html#cross-encoder

    Characteristics of Cross Encoder (a.k.a reranker) models:

Calculates a similarity score given pairs of texts.

Generally provides superior performance compared to a Sentence Transformer (a.k.a. bi-encoder) model.

Often slower than a Sentence Transformer model, as it requires computation for each pair rather than each text.

Due to the previous 2 characteristics, Cross Encoders are often used to re-rank the top-k results from a Sentence Transformer model.




```python
from sentence_transformers import CrossEncoder

# 1. Load a pretrained CrossEncoder model
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

# The texts for which to predict similarity scores
query = "How many people live in Berlin?"
passages = [
    "Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers.",
    "Berlin has a yearly total of about 135 million day visitors, making it one of the most-visited cities in the European Union.",
    "In 2013 around 600,000 Berliners were registered in one of the more than 2,300 sport and fitness clubs.",
]

# 2a. Either predict scores pairs of texts
scores = model.predict([(query, passage) for passage in passages])
print(scores)
# => [8.607139 5.506266 6.352977]

# 2b. Or rank a list of passages for a query
ranks = model.rank(query, passages, return_documents=True)

print("Query:", query)
for rank in ranks:
    print(f"- #{rank['corpus_id']} ({rank['score']:.2f}): {rank['text']}")
"""
Query: How many people live in Berlin?
- #0 (8.61): Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers.
- #2 (6.35): In 2013 around 600,000 Berliners were registered in one of the more than 2,300 sport and fitness clubs.
- #1 (5.51): Berlin has a yearly total of about 135 million day visitors, making it one of the most-visited cities in the European Union.
"""
```


Sparse Encoder Models

Characteristics of Sparse Encoder models:

Calculates sparse vector representations where most dimensions are zero.

Provides efficiency benefits for large-scale retrieval systems due to the sparse nature of embeddings.

Often more interpretable than dense embeddings, with non-zero dimensions corresponding to specific tokens.

Complementary to dense embeddings, enabling hybrid search systems that combine the strengths of both approaches.



```python
from sentence_transformers import SparseEncoder

# 1. Load a pretrained SparseEncoder model
model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

# The sentences to encode
sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
]

# 2. Calculate sparse embeddings by calling model.encode()
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 30522] - sparse representation with vocabulary size dimensions

# 3. Calculate the embedding similarities
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[   35.629,     9.154,     0.098],
#         [    9.154,    27.478,     0.019],
#         [    0.098,     0.019,    29.553]])

# 4. Check sparsity stats
stats = SparseEncoder.sparsity(embeddings)
print(f"Sparsity: {stats['sparsity_ratio']:.2%}")
# Sparsity: 99.84%
```