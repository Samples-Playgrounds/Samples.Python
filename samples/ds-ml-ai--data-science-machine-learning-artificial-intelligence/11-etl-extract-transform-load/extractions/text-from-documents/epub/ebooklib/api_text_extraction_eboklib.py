import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

import os
from pathlib import Path

import traceback
import orjson
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

library_name = "EbookLib"

#@timer()
def extract_text_to_file_from_epub_document (
                                                source_file: str
                                            ) -> str:

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------
    directory = f"{source_file}.hwaifs/extractions/text/py/{library_name}/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    result_txt = ""
    try:
        book = epub.read_epub(source_file)
        num_pages = len(list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT)))

        chapters = []
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                chapters.append(item.get_content())

        for chapter in chapters:
            text = chapter_to_text(chapter)
            result_txt += text + '\n'

    except Exception as e:
        tb = traceback.format_exc()
        msg = \
            f"Exception reading text with {library_name} from EPUB document source = {source_file} : {e}" \
            + \
            tb
        timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
            f.write(msg)
        
        return

    # save to file
    with open(f"{directory}/content.txt", "w") as f:
        f.write(result_txt) 

    #---------------------------------------------------------------------------
    time_stop_1 = time.time()
    time_total_1 = time_stop_1 - time_start_1
    time_stop_2 = perf_counter()
    time_total_2 = time_stop_2 - time_start_2
    time_stop_3 = perf_counter_ns()
    time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000

    times = {
        "function_method_name" : "extract_text_to_file_from_any_document",
        "time_start_1": time_start_1,
        "time_end_1": time_stop_1,
        "time_total_1": time_total_1,
        "time_start_2": time_start_2,
        "time_end_2": time_stop_2,
        "time_total_2": time_total_2,
        "time_start_3": time_start_3,
        "time_end_3": time_stop_3,
        "time_total_3": time_total_3,
        "num_pages" : num_pages,
        "pages_per_second_1" : num_pages / time_total_1,
        "pages_per_second_2" : num_pages / time_total_2,
        "pages_per_second_3" : num_pages / time_total_3,
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.py.json", "w") as f:
        f.write(orjson.dumps(times, option=orjson.OPT_INDENT_2).decode())
    #---------------------------------------------------------------------------

    return result_txt

def chapter_to_text(chap):
    blocklist = ['[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script']
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    prev = ''
    for t in text:
        if t.parent.name not in blocklist:
            if not t.isspace():
                if not (str(prev).endswith(' ') or str(t).startswith(' ')):
                    output += '\n\n'
                output += '{}'.format(t)
            prev = t
    return output
