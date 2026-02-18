

https://github.com/voxserv/audio_quality_testing_samples


https://github.com/colombomf/audio-to-text

https://github.com/javedali99/audio-to-text-transcription

https://stackoverflow.com/questions/32587015/audio-file-to-text-file-python

import speech_recognition as sr
print(sr.__version__)
r = sr.Recognizer()

file_audio = sr.AudioFile('file_audio.wav')

with file_audio as source:
   audio_text = r.record(source)

print(type(audio_text))
print(r.recognize_google(audio_text))


https://stackoverflow.com/questions/54916400/speech-to-text-in-python-with-a-wav-file

https://stackoverflow.com/questions/75794919/how-to-segment-and-transcribe-an-audio-from-a-video-into-timestamped-segments

https://github.com/SupernovifieD/FreeSpeechToText

https://www.geeksforgeeks.org/python/python-convert-speech-to-text-and-text-to-speech/

https://dev.to/ivansing/audio-to-text-using-python-and-openai-3o4f

https://medium.com/@verashoda/transcribing-audio-to-text-in-python-using-whisper-290cea2f6090

https://thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python

https://towardsdatascience.com/transcribing-interview-data-from-video-to-text-with-python-5cdb6689eea1/


video


https://medium.com/@caiomenin/how-to-transcribe-large-video-files-1gb-to-text-with-python-70ba7d13fd27

https://zulko.github.io/moviepy/getting_started/quick_presentation.html

https://amanxai.com/2020/12/25/extract-text-from-videos-using-python/
https://dev.to/stokry/export-text-from-the-video-with-python-34
https://github.com/Jeyashree7/Text-from-Video/blob/main/Code
https://reneelin2019.medium.com/convert-extract-speech-from-video-to-text-with-python-d8ebf4ad9734
    
