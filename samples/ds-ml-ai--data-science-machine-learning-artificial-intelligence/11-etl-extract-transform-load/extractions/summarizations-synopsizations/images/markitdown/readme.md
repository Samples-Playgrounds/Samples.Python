
```python
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI(
	            base_url='http://ollamahost:11434/v1/',
                )
md = MarkItDown(
                llm_client=client,
                llm_model="llama3.2"
                )
result = md.convert("example.jpg")
print(result.text_content)
```

*   https://github.com/microsoft/markitdown/discussions/174

*   https://medium.com/@giacomo__95/markitdown-ollama-and-llava-markdown-conversion-with-microsofts-markitdown-and-ollama-s-llm-2141bba9d183

