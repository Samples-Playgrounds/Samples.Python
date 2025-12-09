from gtts import gTTS

import os
from pathlib import Path

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

#@timer()
def speak (text: str, lang: str = "en", file: str = None  ) -> str:

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    tts = gTTS(text=text, lang=lang, tld="com")
    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    filename = f"tts-audio-{timestamp}.mp3"
    tts.save(filename)
    os.system(f"open {filename}")

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

    #timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    #with open(f"{directory}/performance-data-{timestamp}.python.json", "w") as f:
    #    f.write(json.dumps(times, indent=4))
    #---------------------------------------------------------------------------

    return file
