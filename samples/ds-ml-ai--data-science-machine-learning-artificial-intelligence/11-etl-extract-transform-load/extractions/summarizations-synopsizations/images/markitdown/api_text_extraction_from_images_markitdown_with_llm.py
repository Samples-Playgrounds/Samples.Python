from markitdown import MarkItDown
from openai import OpenAI

import os
from pathlib import Path

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

#@timer()
def summarize_image (source: str) -> str:

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/text/python/easyocr/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # Set Ollama API base URL for using a vision model
    #os.environ['OLLAMA_API_BASE'] = "http://localhost:11434"

    client = OpenAI(
                    #base_url='http://ollamahost:11434/v1/',
                    base_url='http://localhost:11434/v1/',
                    api_key='ollama',  # Required, but not used for local models
                    )


    md = MarkItDown(
                    llm_client=client,
                    llm_model="llama3.2-vision:latest"
                    #llm_model="llava:34b"
                    )


    result = md.convert(source)

    text_complete = result.text_content

    # save to file
    with open(f"{directory}/summary.md", "w") as f:
        f.write(text_complete) 

    #---------------------------------------------------------------------------
    time_stop_1 = time.time()
    time_total_1 = time_stop_1 - time_start_1
    time_stop_2 = perf_counter()
    time_total_2 = time_stop_2 - time_start_2
    time_stop_3 = perf_counter_ns()
    time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000

    times = {
        "function_method_name" : "summarize_image",
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
    with open(f"{directory}/performance-data-{timestamp}.python.json", "w") as f:
        f.write(json.dumps(times, indent=4))
    #---------------------------------------------------------------------------

    return text_complete