"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install gTTS
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_tts_text_to_speech_TTS as api


# document per local path or URL
sources = [
   "Hi Moljac. What's up?",
]

def main():
   for source in sources:
      print(f"gTTS <- source = {source}")
      api.speak(source)


if __name__ == '__main__':
    main()

