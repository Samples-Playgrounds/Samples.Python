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

youtube_video_ids = [
    "iybdUPYXPEw",
    "845fNBa_R_4",
    "JuXgIqZjRBQ",
    "OOcv9Mj0Fsc",
    "DlsTxZdgklw",
    "OOcv9Mj0Fsc",
    "ck5nw7R1uEs",
    "x37O-PUBvw0",
    "WqFt6YHHy50",
    "nUlomY7RsIg",
    "T__1QViXUxk",
#    "",
]

import json
import jsonpickle


from youtube_transcript_api import YouTubeTranscriptApi

def main():
    for youtube_video_id in youtube_video_ids:
        print(f"yt <- youtube_video_ids = {youtube_video_ids}")

        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(youtube_video_id)

        transcript = ""
        for fetched_transcript_snippet in fetched_transcript :
            transcript += "\n" + fetched_transcript_snippet.text

        directory = "./"
        with open(f"{directory}/youtube-video-transcript-{youtube_video_id}.txt", "w") as f:
            f.write(transcript) 

        # json_dump_fetched_transcript = json.dumps(fetched_transcript)
        # txt_json = jsonpickle.encode(fetched_transcript)
        #print("=" * 120)
        #print(json_dump_fetched_transcript)

        print("=" * 120)
        print(fetched_transcript)
        print("=" * 120)
        print(transcript)

if __name__ == '__main__':
    main()


