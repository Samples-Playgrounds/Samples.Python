from PyPDF2 import PdfReader

from pathlib import Path

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

#@timer()
def extract_images_from_pdf_to_files (source: str) -> str:
    """
    """

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/images/py/PyPDF2-pypdf/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    reader = PdfReader(source)

    page_no = 1
    for page in reader.pages:
        img_no = 1
        images = []
        # https://pypdf2.readthedocs.io/en/3.0.0/modules/PageObject.html#PyPDF2._page.PageObject.images
        try:
            images.extend(page.images)
        except ValueError:
            images = []

        for image in images:
            name = image.name
            with open(f"{directory}/p{page_no}-{img_no}-{name}", "wb") as fp:
                fp.write(image.data)
            img_no += 1
        page_no += 1

    #---------------------------------------------------------------------------
    time_stop_1 = time.time()
    time_total_1 = time_stop_1 - time_start_1
    time_stop_2 = perf_counter()
    time_total_2 = time_stop_2 - time_start_2
    time_stop_3 = perf_counter_ns()
    time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000

    times = {
        "function_method_name" : "extract_images_from_pdf_to_files",
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

