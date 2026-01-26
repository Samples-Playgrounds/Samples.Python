from deepfake_detector import DeepfakeDetector

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

# Create a detector object with a custom threshold
detector = DeepfakeDetector(threshold=0.5)

#@timer()
def detect_deepfake_from_image (source: str) -> str:
    """
    """

    # Detect deepfakes in an image

    result = detector.detect_from_image('path_to_image.jpg')
    return f"The image {source} is classified as: {"FAKE" if result > 0.5 else "REAL"}"

