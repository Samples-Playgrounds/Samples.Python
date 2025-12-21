
def split_chunks_on_character_count (
                                        text: str,
                                        size_chunk: int = 100 
                                    ) -> [] :
    """
    """
    
    result = []
    for i in range(0, len(text), size_chunk):
        result.append(text[i:i + size_chunk])
        
    return result


def split_chunks_on_character_count_with_overlap (
                                                    text: str, 
                                                    size_chunk: int = 100,
                                                    size_overlap: int = 0
                                                ) -> []:
    """
    """
    
    result = []
    for i in range(0, len(text),size_chunk):
        b = i
        e = b + size_chunk - size_overlap
        result.append(text[b:e])
        b = 

    return result
