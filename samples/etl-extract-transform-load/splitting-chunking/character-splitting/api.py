
def split_on_character (text: str, size_chunk: int = 35) -> []:
    result = []
    for i in range(0, len(text), size_chunk):
        result.append(text[i:i + size_chunk])
    return result
