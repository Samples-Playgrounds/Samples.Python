"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install pyttsx3
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_tts_text_to_speech_python_espeak as api


# document per local path or URL
sources = [
   "Hi Moljac. What's up?",
]

def main():
   for source in sources:
      print(f"pyttsx3 <- source = {source}")
      api.speak(source)


if __name__ == '__main__':
    main()

