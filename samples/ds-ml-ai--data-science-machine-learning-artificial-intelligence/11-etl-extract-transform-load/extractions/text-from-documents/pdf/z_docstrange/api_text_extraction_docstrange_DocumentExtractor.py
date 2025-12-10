from docstrange import DocumentExtractor

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

#@timer()
def extract_markdown_to_file_from_pdf_document (source: str) -> str:

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    # Initialize extractor (cloud mode by default)
    extractor = DocumentExtractor()

    # Convert any document to clean markdown
    result = extractor.extract(source)
    result_md = result.extract_markdown()
    print(result_md)

    directory = f"{source}.hwaifs/text/python/docstrange/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}/content.md", "w") as f:
        f.write(result_md)

    #---------------------------------------------------------------------------
    time_stop_1 = time.time()
    time_total_1 = time_stop_1 - time_start_1
    time_stop_2 = perf_counter()
    time_total_2 = time_stop_2 - time_start_2
    time_stop_3 = perf_counter_ns()
    time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000

    times = {
        "function_method_name" : "extract_markdown_to_file_from_pdf_document",
        "num_pages" : num_pages,
        "time_start_1": time_start_1,
        "time_end_1": time_stop_1,
        "time_total_1": time_total_1,
        "pages_per_second_1" : num_pages / time_total_1,
        "time_start_2": time_start_2,
        "time_end_2": time_stop_2,
        "time_total_2": time_total_2,
        "pages_per_second_2" : num_pages / time_total_2,
        "time_start_3": time_start_3,
        "time_end_3": time_stop_3,
        "time_total_3": time_total_3,
        "pages_per_second_3" : num_pages / time_total_3
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.python.json", "w") as f:
        f.write(json.dumps(times, indent=4))
    #---------------------------------------------------------------------------

    return result_md
