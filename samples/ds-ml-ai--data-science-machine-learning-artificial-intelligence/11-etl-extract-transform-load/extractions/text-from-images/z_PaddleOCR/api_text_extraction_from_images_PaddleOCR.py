from paddleocr import PaddleOCR

import os
from pathlib import Path

import traceback
import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

import paddle
paddle.utils.run_check()

#@timer()
def extract_text_to_file_from_image (source: str) -> str:
    """
    https://www.paddleocr.ai/main/en/index.html
    
    Extract text from image using PaddleOCR and save results to file.
    """

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/text/py/PaddleOCR/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    result_txt = ""

    try:
        # Initialize PaddleOCR instance
        ocr = PaddleOCR(
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False
            )

        # Run OCR inference on a sample image 
        result = ocr.predict(
            source
            # input="https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png"
            )
        for res in result:
            result_txt += res["text"] + "\n"
            # res.print()
            # res.save_to_img("output")
            # res.save_to_json("output")

    except Exception as e:
        tb = traceback.format_exc()
        msg = \
            f"Exception extracting images from PDF document source = {source} : {e}" \
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
        "function_method_name" : "extract_text_to_file_from_image",
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

    return result_txt
