import commonmark
import html_to_json

import os
from pathlib import Path

import traceback
import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

#@timer()
def api_parse_analyze_markdown_commonmark (source: str) -> str:
    """
    """
    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/parse-analysis/py/commonmark/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    paragraphs = []

    try:
        parser = commonmark.Parser() 

        with open(source, 'r') as f:
            text = f.read()

        ast = parser.parse(text)

        for node in ast.walker():
            if node[0].t == "paragraph":
                paragraphs.append(node[0].first_child.literal)

        renderer = commonmark.HtmlRenderer()
        html = renderer.render(ast)
        html_json = html_to_json(html)
        
    except Exception as e:
        tb = traceback.format_exc()
        msg = \
            f"Exception parsing markdown with commonmark = {source} : {e}" \
            + \
            tb
        timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
            f.write(msg)
        
        return paragraphs

    with open(f"{directory}/content.html", "w") as f:
        f.write(html)

    with open(f"{directory}/paragraphs.json", "w") as f:
        f.write(json.dumps(paragraphs, indent=4))

    with open(f"{directory}/html.json", "w") as f:
        f.write(json.dumps(html_json, indent=4))

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

    return paragraphs


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
