
import os
from pathlib import Path

import traceback
import orjson
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

library_name = "stdlib"

tokens_per_word = {
                        "en":   ( 0.75, 0.75, 4 ),
                        "de":   ( 2.1, 2.1, 3 ),
                        "hr":   ( 1.5, 2.0, 3.2 ),
                }

def tokens_characters_in_text (
                                text: str,
                                language: str = None
                                ) -> str:
    """
    """
    if language is None:
        language = "en"

    t = tokens_per_word[language]

    characters = list(text)
    count_characters = len(characters)
    count_tokens = int(count_characters / t[2])

    return (characters, count_characters, count_tokens)



def tokens_words_in_text (
                                text: str,
                                language: str = None
                                ) -> str:
    """
    """
    if language is None:
        language = "en"

    tuple = tokens_per_word.get(language)

    words = text.split()
    count_words = len(words)    
    count_tokens_min = int(len(words) * tuple[0])
    count_tokens_max = int(len(words) * tuple[1])

    return (words, count_words, count_tokens_min, count_tokens_max)


def tokens_characters_in_file (
                                file_path: str
                                ) -> str:
    """
    """
    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------
