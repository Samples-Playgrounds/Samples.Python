# Summarizer Synopsiszer Refiner

*   https://heartbeat.comet.ml/text-summarization-using-python-and-nltk-d1022ac347eb

*   https://www.turing.com/kb/5-powerful-text-summarization-techniques-in-python

*   https://www.geeksforgeeks.org/nlp/mastering-text-summarization-with-sumy-a-python-library-overview/

*   https://medium.com/@ryver.dev/building-a-simple-ai-powered-text-summarizer-with-transformers-in-python-0a31c848e1d2

*   https://medium.com/p/b3b260c60e72

*   https://medium.com/data-science/summarize-a-text-with-python-continued-bbbbb5d37adb

*   https://stackabuse.com/text-summarization-with-nltk-in-python/

*   https://stackabuse.com/python-for-nlp-tokenization-stemming-and-lemmatization-with-spacy-library/

*   https://medium.com/@tebugging/summarize-any-text-based-document-with-8-lines-of-python-and-llamaindex-17335986877b

    *   https://github.com/tjaensch/llamaindex_summarize_custom_docs

*   https://www.geeksforgeeks.org/nlp/text-summarization-in-nlp/

*   https://stackoverflow.com/questions/5479333/what-are-the-available-tools-to-summarize-or-simplify-text

*   https://github.com/colombomf/text-summarizer

*   https://www.kaggle.com/code/imkrkannan/text-summarization-with-nltk-in-python

*   https://www.linkedin.com/pulse/create-your-own-custom-text-summarization-tool-python-russell-phd-ywxec/

*   https://pypi.org/project/summa/

*   Summarize Any Text in Minutes with Python Natural Language Processing NLP!
    
    *   https://www.youtube.com/watch?v=DEok-uVND2w

*   Summarize Text in Python Using ChatGPT (and other NLP tasks)

    *   https://www.youtube.com/watch?v=Aqpi6abDAiM

*   How to Summarize Text Using Python and Machine Learning

    *   https://www.youtube.com/watch?v=SNimr_nOC7w

*   Create Your First AI Text Summarization Tool with Langchain: Ultimate Beginner Tutorial!

    *   https://www.youtube.com/watch?v=GRtZjIUW-Z0
    
*   Build a local Document Summarizer AI Agent with Ollama and Llama 3.1 in 10 Minutes

    *   https://www.youtube.com/watch?v=VDVwsiOQj_E

        *   ollama

        *   llama3.1

        *   python

*   Summarize PDFs with a Local AI (Private GPT) in Python

    *   https://www.youtube.com/watch?v=Tnu_ykn1HmI

    *   https://github.com/Vincent-Codes-Finance/documents-llm

    *   provider/host
    
        *   ollama

    *   mixtral

    Summarize Hundreds of PDFs with Local AI Python Automation (Ollama + Gemma 3)
    https://www.youtube.com/watch?v=rxGVLSlUfaQ
    


    """
    Write long document summary of the following document.
    Include only information that is part of the document.
    Do not include other/external information.
    Do not include personal opinion or analysis.
    """


```
pip \
    install \
        langchain \
        langchain_openai \
        langchain_community \
        requests \
        bs4 \
        duckduckgo-search
```


*   https://www.reddit.com/r/LocalLLaMA/comments/1891o5m/whats_the_best_llm_for_summarization_of_long/

    BERT

    RoBERTa

    https://huggingface.co/jondurbin

        Airoboros

    

    extension for text-generation-webui that automatically chunks and summaries a document you paste in.

There's some projects that are working on similar stuff on the backend (LangChain, LlamaIndex,txtai) and you can use LocalAI or llama-cpp-python server or whatever as an OpenAI API replacement if you've got a tool that talks to that. But I'm not aware of any good front-end interfaces. (There's paperai and Neurite and stuff, but those are relatively narrowly focused, I think?)

you can use any abstractive summarization model,

i use BERT it does what i need, my workflow is:

get html content from url (request + bs4)

get main content (newspaper + readability)

convert to text (lxml)

clean the text (unicodedata)

split to chunks

summarize using any abstractive model in batches

join summarized chunks

YI-34B with 200k of context.

https://huggingface.co/brucethemoose/CaPlatTessDolXaBoros-Yi-34B-200K-DARE-Ties-HighDensity
https://huggingface.co/brucethemoose/CapyTessBorosYi-34B-200K-DARE-Ties
https://huggingface.co/dphn/dolphin-2_2-yi-34b

