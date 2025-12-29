# Splitting - Chunking

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

https://medium.com/@jagadeesan.ganesh/understanding-chunking-algorithms-and-overlapping-techniques-in-natural-language-processing-df7b2c7183b2

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