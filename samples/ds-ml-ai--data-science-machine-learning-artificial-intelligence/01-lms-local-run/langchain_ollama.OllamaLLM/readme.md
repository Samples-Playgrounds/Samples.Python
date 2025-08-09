# llama_index.text_splitter-SentenceSplitter

readme.md


```shell
python3.13 -m venv .venv
source .venv/bin/activate
pip3.13 install "langchain_ollama"
pip3.13 freeze > requirements.txt
```



```python
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.1:8b")

llm.invoke("The first man on the moon was ...")
```

*   https://python.langchain.com/docs/how_to/local_llms/
