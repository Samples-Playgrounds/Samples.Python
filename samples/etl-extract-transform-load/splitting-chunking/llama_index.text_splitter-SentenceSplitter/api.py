from llama_index.core.node_parser import SentenceSplitter


def split_text (text: str, size_chunk: int = 35, chunk_overlap: int = 0) -> []:
    splitter = SentenceSplitter(
        chunk_size=size_chunk,
        chunk_overlap=chunk_overlap,
    )

    nodes = splitter.get_nodes_from_documents(text)

    return nodes