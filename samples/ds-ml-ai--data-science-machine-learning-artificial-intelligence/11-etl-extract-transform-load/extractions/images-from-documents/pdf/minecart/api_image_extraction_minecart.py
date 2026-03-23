import minecart
import PIL

from pathlib import Path
import traceback

import orjson
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

library_name = "minecart"

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

    pdffile = open(source_file, 'rb')
    doc = minecart.Document(pdffile)

    num_pages = 1
    try:
        for page in doc.iter_pages():
            img_no = 1
            for i in range(len(page.images)):
                im1 = page.images[i]
                im = im1.as_pil()  # requires pillow
                im.save(f"{directory}/img-p{num_pages}-{img_no}.jpg")

                img_no += 1

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

