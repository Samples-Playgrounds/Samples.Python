import minecart
import PIL

from pathlib import Path
import traceback

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

    directory = f"{source}.hwaifs/images/py/minecart/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    pdffile = open(source, 'rb')
    doc = minecart.Document(pdffile)

    page_no = 1
    try:
        for page in doc.iter_pages():
            img_no = 1
            for i in range(len(page.images)):
                try:
                    im1 = page.images[i]
                    im = im1.as_pil()  # requires pillow
                    im.save(f"{directory}/img-p{page_no}-{img_no}.jpg")
                except Exception as e:
                    print(e)
                    print(f"Error encountered at {source}, p {page_no}, img {img_no}")
                    traceback.print_exc()

                img_no += 1
    except Exception as e1:
        print(f"Error encountered at {source}")

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

