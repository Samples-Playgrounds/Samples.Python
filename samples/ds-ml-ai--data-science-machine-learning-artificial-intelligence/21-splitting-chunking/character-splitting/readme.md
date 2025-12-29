# Character Splitting

readme.md

Levels of Text Splitting/Chunking:

1.  Character Splitting

    *   Split by fixed character length.

2.  Recursive Character

    *   split by series of separators.

3.  Document Specific

    *   Various chunking methods for different document types

4.  Semantic

    *   Embedding based chunking

5.  Agentic

    *   Agent like decision when to split.

*   https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb

*   https://www.reddit.com/r/LocalLLaMA/comments/15mq1ri/what_are_the_text_chunkingsplitting_and_embedding/

    *   optimal 512

    *   [50, 5000]

*   https://medium.com/@263akash/different-levels-of-text-splitting-chunking-ce9da78570d5

*   https://www.geeksforgeeks.org/data-analysis/how-to-chunk-text-data-a-comparative-analysis/

*   https://www.analyticsvidhya.com/blog/2025/02/types-of-chunking-for-rag-systems/

*   https://www.reddit.com/r/LangChain/comments/15mq21r/what_are_the_text_chunkingsplitting_and_embedding/

*   https://graphrag.com/guides/chunking/

*   https://latenode.com/blog/ai-frameworks-technical-infrastructure/rag-retrieval-augmented-generation/rag-chunking-strategies-complete-guide-to-document-splitting-for-better-retrieval

*   https://community.fullstackretrieval.com/document-loaders/text-splitting

*   https://successive.tech/blog/rag-models-optimizing-text-input-chunking-splitting-strategies/

*   https://avestalabs.ai/blog/llm-based-chunking-intelligent-text-splitting-for-better-rag

*   https://www.pinecone.io/learn/chunking-strategies/

## Code Snipetts

*   https://github.com/luay458/taia_tool/blob/master/app/services/ingestion.py#L59

*   https://github.com/Nabeel-Ahsan7/Multilingual-RAG-System/blob/b5750fa6296f7a635da5494743fe5dc0671bdef8/FAQ.md?plain=1#L105

*   https://github.com/UdeeshaRukshan/Assignment2/blob/4e0fb79c6845766e04d7b4e9abd1fb62ca5c9b89/docs.md?plain=1#L118

### RAG

https://github.com/llmware-ai/llmware

https://github.com/snexus/llm-search


*   ada-002

    *   performs badly for German and Multilingual Embeddings for RAG workflows.

*   Sentence-Transformer using SOTA models from the MTEB leaderboard.

*   Embedding Models performing very well:

    *   e5-large-v2

    *   instructor-large

    *   multilingual-e5-large

The implementations for business clients usually involve:

Azure OpenAI GPT-4 endpoint

Either ada-002 endpoint hosted on Azure or selfhosted embedding model endpoint

Microsoft BotFramework for orchestration of flows

LangChain for calling emedding APIs and summon agents



## Structure

### PDF

```shell
find ./text -type f -iname "*.txt" -o -iname "*.md"
```

```shell
./text/python/pymupdf4llm/content.md
./text/python/pdfplumber/content.txt
./text/python/markitdown/content.md
./text/python/docling/content.txt
./text/python/docling/content.md
./text/python/docling/content.filetype-agnostic.md
./text/python/PyMuPDF_fitz/content.txt
./text/python/PyPDF2/content.txt
./text/python/pdfminer_six/content.txt
./text/python/unstructured/content.txt
./text/python/marker/content.md
./text/python/pypdfium2/content.txt
./text/python/pytesseract/content.txt
```
