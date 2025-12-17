

pyspeech and speech_recognition

https://pypi.org/project/SpeechRecognition/

```python
import speech_recognition as sr
print(sr.__version__)
r = sr.Recognizer()

file_audio = sr.AudioFile('file_audio.wav')

with file_audio as source:
   audio_text = r.record(source)

print(type(audio_text))
print(r.recognize_google(audio_text))
```

https://pythonbasics.org/transcribe-audio/





https://github.com/jiaaro/pydub

https://stackoverflow.com/questions/61787629/convert-sound-from-website-to-text-in-python

https://stackoverflow.com/questions/54916400/speech-to-text-in-python-with-a-wav-file






https://github.com/openai/whisper

https://medium.com/@verashoda/transcribing-audio-to-text-in-python-using-whisper-290cea2f6090



https://github.com/SupernovifieD/FreeSpeechToText


https://thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python

pip install librosa numpy scipy SpeechRecognition

pip3 install SpeechRecognition pydub

import speech_recognition as sr

https://towardsdev.com/using-python-to-extract-text-from-audio-57405e31a117

https://www.jeremymorgan.com/tutorials/generative-ai/how-to-transcribe-audio/

https://www.geeksforgeeks.org/python/python-convert-speech-to-text-and-text-to-speech/
