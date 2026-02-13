"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install youtube-transcript-api
pip install jsonpickle
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_text_extraction_video_youtube_transcript as api

import sys
import os
scriptpath = "../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *


def main():
    for youtube_video_id in youtube_video_ids:
        print(f"yt <- youtube_video_ids = {youtube_video_ids}")

        transcript = api.extract_text_transcript_from_video_youtube_to_file(
                                                                                youtube_video_id,
                                                                                directory="../../../../../../data/videos/"
                                                                            )
        print("=" * 120)
        print(transcript)

if __name__ == '__main__':
    main()


