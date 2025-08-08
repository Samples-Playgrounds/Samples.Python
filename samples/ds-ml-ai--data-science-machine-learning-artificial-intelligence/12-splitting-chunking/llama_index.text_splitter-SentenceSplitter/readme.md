# llama_index.text_splitter-SentenceSplitter

readme.md

*   https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb

*   https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/

```shell
python3.13 -m venv .venv
source .venv/bin/activate
pip3.13 install "llama_index"
pip3.13 freeze > requirements.txt
```



```python
from llama_index.text_splitter import SentenceSplitter
from llama_index import SimpleDirectoryReader

# Load up your splitter

splitter = SentenceSplitter(
    chunk_size=200,
    chunk_overlap=15,
)

# Load up your document

documents = SimpleDirectoryReader(
    input_files=["../../data/PGEssays/mit.txt"]
).load_data()

# Create your nodes. Nodes are similar to documents but with more relationship data added to them.

nodes = splitter.get_nodes_from_documents(documents)
```
