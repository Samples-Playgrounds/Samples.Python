import os
from pathlib import Path

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

def text_split_chunks_on_character_count (
                                            text: str, 
                                            size_chunk: int = 1000
                                        ) -> []:
    """
    Splits text into chunks of a specified character.
    """
    
    result = []
    for i in range(0, len(text), size_chunk):
        b = i
        e = b + size_chunk
        result.append(text[b:e])

    return result

import json

def file_split_chunks_on_character_count (
                                            file_name: str, 
                                            size_chunk: int = 1000
                                        ) -> []:
    """
    Splits text into chunks of a specified character.
    """

    if (file_name is None) or (not os.path.isfile(file_name)):
        # raise ValueError("file_name must be a valid file path.")
        print(f"Error not found {file_name}")
        return None

    directory = f"{file_name}.hwaifs/{file_name}.hwaifs/splits-chunks/py/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()

    result = text_split_chunks_on_character_count(text, size_chunk)

    file_name_result = f"{directory}/chunks_on_character_count-{size_chunk}.txt"
    with open(file_name_result, 'w', encoding='utf-8') as f:
        f.write(str(result))

    file_name_result = f"{directory}/chunks_on_character_count-{size_chunk}.json"
    with open(file_name_result, 'w', encoding='utf-8') as f:
        json.dump(result, f)

    return result
