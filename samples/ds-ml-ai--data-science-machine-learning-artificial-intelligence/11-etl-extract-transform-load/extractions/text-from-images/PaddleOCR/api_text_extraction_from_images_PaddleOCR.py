from paddleocr import PaddleOCR

import os
from pathlib import Path

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

#@timer()
def extract_text_to_file_from_image (source: str) -> str:
    """
    https://www.paddleocr.ai/main/en/index.html
    
    Extract text from image using PaddleOCR and save results to file.
    """


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

    # Visualize the results and save the JSON results
    for res in result:
        res.print()
        res.save_to_img("output")
        res.save_to_json("output")
    
