import fitz as mu  # PyMuPDF

from pathlib import Path
import traceback

import orjson
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

library_name = "PyMuPDF-fitz"

#@timer()
def extract_images_from_pdf_to_files (
                                        source_file: str
                                    ) -> str:
    """
    """
    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------
    directory = f"{source_file}.hwaifs/extractions/images/py/{library_name}/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    num_pages = 0
    try:
        with mu.open(source_file) as pdf:
            for page in pdf:
                for info in page.get_images(full=True):
                    xref = info[0]
                    img = pdf.extract_image(xref)

                    ext, data = img['ext'], img['image']

                    with open(f'{directory}/{xref}.{ext}', 'wb') as f:
                        f.write(data)
            
                num_pages += 1
    except Exception as e:
        tb = traceback.format_exc()
        msg = \
            f"Exception reading images with {library_name} from PDF document source = {source_file} : {e}" \
            + \
            tb
        timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
            f.write(msg)

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
        "num_pages" : num_pages,
        "pages_per_second_1" : num_pages / time_total_1,
        "pages_per_second_2" : num_pages / time_total_2,
        "pages_per_second_3" : num_pages / time_total_3,
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.py.json", "w") as f:
        f.write(orjson.dumps(times, option=orjson.OPT_INDENT_2).decode())
    #---------------------------------------------------------------------------
