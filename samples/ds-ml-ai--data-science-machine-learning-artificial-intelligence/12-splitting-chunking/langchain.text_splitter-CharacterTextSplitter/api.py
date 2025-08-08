
from langchain.text_splitter import CharacterTextSplitter

def split_on_character (text: str, 
                        size_chunk: int = 35,
                        chunk_overlap:int = 0, 
                        separator: str = '', 
                        strip_whitespace: bool = False
                        ) -> []:
    text_splitter = CharacterTextSplitter(chunk_size=size_chunk, chunk_overlap=chunk_overlap, separator=separator, strip_whitespace=strip_whitespace)
    chunks = text_splitter.split_text(text)
    return chunks