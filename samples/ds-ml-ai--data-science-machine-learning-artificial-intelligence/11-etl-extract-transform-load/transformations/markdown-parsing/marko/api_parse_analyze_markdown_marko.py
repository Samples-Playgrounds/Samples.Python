import marko

import traceback
import os
from pathlib import Path

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

def api_parse_analyze_markdown_marko (source: str) -> str:
    """
    """
    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/parse-analysis/py/marko/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    try:
        with open(source, 'r') as f:
            text = f.read()

        # Convert markdown to HTML
        html = marko.convert(text)

        # marko.block.Document
        # https://marko-py.readthedocs.io/en/latest/api.html#marko.parser.Parser.parse
        doc = marko.parse(text)
        # list[BlockElement]
        # elements = marko.parse_source(text)

        # tokens = []
        # for token in doc:
        #     tokens.append(token)

    except Exception as e:
        tb = traceback.format_exc()
        msg = \
            f"Exception parsing markdown with marko = {source} : {e}" \
            + \
            tb
        timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
            f.write(msg)

        return


    with open(f"{directory}/content.html", "w") as f:
        f.write(html)

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
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.py.json", "w") as f:
        f.write(json.dumps(times, indent=4))
    #---------------------------------------------------------------------------

    return doc


import json
from bs4 import BeautifulSoup

def html_to_json(html: str) -> dict:
    soup = BeautifulSoup(html, 'lxml')
    
    data = {}
    for tag in soup.find_all():
        if not tag.name in data:
            data[tag.name] = []
        
        attrs = {k: v for k, v in tag.attrs.items()}
        data[tag.name].append(attrs)
    
    return data
