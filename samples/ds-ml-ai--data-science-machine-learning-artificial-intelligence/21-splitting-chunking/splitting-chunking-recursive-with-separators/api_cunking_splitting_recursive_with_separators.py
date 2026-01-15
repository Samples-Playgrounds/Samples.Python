import os
from pathlib import Path

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

def text_split_chunks_on_word_count_with_overlap (
                                        text: str,
                                        size_chunk: int = 500,
                                        size_overlap: int = 50

                                    ) -> [] :
    """
    Splits text into chunks of a specified word count with overlap.
    """
    
    words = text.split()
    result = []
    for i in range(0, len(words), size_chunk - size_overlap):
        result.append(' '.join(words[i:i + size_chunk]))

    return result


import json

def file_split_chunks_on_word_count_with_overlap (
                                                    text: str,
                                                    size_chunk: int = 500,
                                                    size_overlap: int = 50

                                                ) -> [] :
    """
    Splits file into chunks of a specified word count with overlap.
    """
    
    if (file_name is None) or (not os.path.isfile(file_name)):
        # raise ValueError("file_name must be a valid file path.")
        print(f"Error not found {file_name}")
        return None

    directory = f"{file_name}.hwaifs/{file_name}.hwaifs/splits-chunks/py/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()

    result = text_split_chunks_on_word_count_with_overlap(text, size_chunk, size_overlap)

    file_name_result = f"{directory}/chunks_on_word_count_with_overlap-{size_chunk}-{size_overlap}.txt"
    with open(file_name_result, 'w', encoding='utf-8') as f:
        f.write(str(result))

    file_name_result = f"{directory}/chunks_on_word_count_with_overlap-{size_chunk}-{size_overlap}.json"
    with open(file_name_result, 'w', encoding='utf-8') as f:
        json.dump(result, f)

    return result
