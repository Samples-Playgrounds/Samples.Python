# Splitting - Chunking

# Splitting/Chunking

readme.md

*   https://docs.langchain.com/oss/python/integrations/splitters

Levels of Text Splitting/Chunking:

1.  Splitting/Chunking by characters or words

    *   Split by fixed character or word count/length with or without overlap

2.  Recursive Character

    *   split by series of separators.

3.  Document Specific

    *   Various chunking methods for different document types

4.  Semantic

    *   Embedding based chunking

    *   *   https://medium.com/@hasanaboulhassan_83441/semantic-chunking-definitive-guide-free-python-code-included-a06044ab0543

    *   https://www.reddit.com/r/LangChain/comments/1erxo60/a_guide_to_understand_semantic_splitting_for/

    *   There is a SMARTER way to split your documents for GenAI apps
    
        *   https://youtube.com/watch?v=qvDbOYz6U24&feature=youtu.be

    https://www.reddit.com/r/LangChain/comments/1gmlocz/semantic_chunking_smarter_text_division_for/

    https://www.reddit.com/r/Python/comments/1ij1fk7/semanticchunker_v020_typesafe_structurepreserving/
    
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

*   5 Levels of Text Splitting

    *   https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb

*   The 5 Levels Of Text Splitting For Retrieval

    *   https://www.youtube.com/watch?v=8OJC21T2SL4&ab_channel=GregKamradt

*   https://chunkviz.up.railway.app/

*   But, How is Chunking Done ? Splitting Basics Using LangChain

    *   https://youtu.be/tMwdl9hFPns

*   Langchain Text Splitters (Chunking) for Beginners | 6 Examples!

    *   https://www.youtube.com/watch?v=Io43kf0hYn4&ab_channel=Ryan%26MattDataScience

*   Why Your RAG Gives Wrong Answers (And 4 Chunking Strategies to Fix It) | LangChain Text Splitters

    *   https://www.youtube.com/watch?app=desktop&v=Lk6D1huUK0s&t=986s&ab_channel=VenelinValkov

*   https://www.reddit.com/r/Rag/comments/1mtcvs7/the_beauty_of_parentchild_chunking_graph_rag_was/

```shell
pip install langchain
pip install tiktoken
```

*   https://www.geeksforgeeks.org/data-analysis/how-to-chunk-text-data-a-comparative-analysis/

*   https://medium.com/@jagadeesan.ganesh/understanding-chunking-algorithms-and-overlapping-techniques-in-natural-language-processing-df7b2c7183b2


## code chunking

*   https://code2prompt.dev/docs/tutorials/getting_started/

*   https://python.langchain.com/docs/how_to/code_splitter/

*   https://python.langchain.com/docs/how_to/code_splitter/#c

*   https://python.langchain.com/docs/how_to/code_splitter/#markdown

*   https://python.langchain.com/docs/how_to/code_splitter/#python

## Structure

### PDF

```shell
find ./text -type f -iname "*.txt" -o -iname "*.md"
```

PDF:

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

Microsoft Word docx:

```shell
./text/python/pymupdf4llm/content.md
./text/python/docx2txt/content.txt
./text/python/markitdown/content.md
./text/python/docling/content.txt
./text/python/docling/content.md
./text/python/docling/content.filetype-agnostic.md
./text/python/docx/content.txt
./text/python/docx2python/content.txt
```