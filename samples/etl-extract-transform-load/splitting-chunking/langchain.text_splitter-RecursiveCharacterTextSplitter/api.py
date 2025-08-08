from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text (text: str, size_chunk: int = 35, chunk_overlap: int = 0) -> []:
    text_splitter = RecursiveCharacterTextSplitter(
                                            chunk_size = size_chunk,
                                            chunk_overlap= chunk_overlap)
    
    documents = text_splitter.create_documents([text])

    return documents