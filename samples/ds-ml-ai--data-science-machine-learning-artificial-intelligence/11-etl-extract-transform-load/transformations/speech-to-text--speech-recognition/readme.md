
https://realpython.com/python-speech-recognition/


```python
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

#Create Recognizer() class objects called recog1 and recog2
recog1 = spr.Recognizer()
recog2 = spr.Recognizer()

#Create microphone instance with device microphone chosen whose index value is 0
mc = spr.Microphone(device_index=0)

#Capture voice
with mc as source:
    print("Speak 'Hello' to initiate the Translation!")
    print("----------------------------")
    audio = recog1.listen(source)
#Based on speech, tranlate the sentence into another language
if 'hello' in recog1.recognize_google(audio):
    recog1 = spr.Recognizer()
    translator = Translator()
    from_lang = 'en'
    to_lang = 'hi'
    with mc as source:
        print('Speak a sentence...')
        audio = recog2.listen(source)
        get_sentence = recog2.recognize_google(audio)
        
        try:
            get_sentence = recog2.recognize_google(audio)
            print('Phrase to be Tranlated: '+ get_sentence)
            text_to_translate = translator.translate(get_sentence, src = from_lang, dest = to_lang)
            text = text_to_translate.text
            speak = gTTS(text=text, lang = to_lang, slow = False)
            speak.save("captured_voice.mp3")
            os.system("start captured_voice.mp3")
        except spr.UnknownValueError:
            print("Unable to understand the input")
        except spr.RequestError as e:
            print("Unable to provide required output".format(e))
```

```python
import speech_recognition as sr
import sounddevice as sd
import numpy as np
from gtts import gTTS
import playsound
import webbrowser
import os
import tempfile

def talk(text, lang="en"):
    print("[AI]:", text)
    tts = gTTS(text=text, lang=lang)
    tmp_file = tempfile.mktemp(suffix=".mp3")
    tts.save(tmp_file)
    playsound.playsound(tmp_file)
    os.remove(tmp_file)

def listen_command():
    recognizer = sr.Recognizer()
    duration = 5
    fs = 16000
    print("Speak...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    audio = sr.AudioData(np.array(audio_data).tobytes(), fs, 2)

    try:
        command = recognizer.recognize_google(audio, language="en-US").lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        talk("could you repeat")
        return ""
    except sr.RequestError:
        talk("Speech recognition service error")
        return ""

while True:
    cmd = listen_command()
    if not cmd:
        continue

    if "youtube" in cmd:
        talk("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "google" in cmd:
        talk("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "stop" in cmd or "exit" in cmd or "close" in cmd:
        talk("Goodbye calmoev!")
        break

    else:
        talk("Command not recognized")
```