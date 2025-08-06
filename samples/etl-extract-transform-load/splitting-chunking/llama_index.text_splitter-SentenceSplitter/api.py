
from llama_index.text_splitter import SentenceSplitter
from llama_index import SimpleDirectoryReader


def split_on_character (text: str, size_chunk: int = 35) -> []:
    splitter = SentenceSplitter(
        chunk_size=200,
        chunk_overlap=15,
    )
