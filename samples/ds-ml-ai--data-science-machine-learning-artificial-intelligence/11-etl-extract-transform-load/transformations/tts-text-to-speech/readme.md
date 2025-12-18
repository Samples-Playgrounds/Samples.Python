# TTS Text to Speech

*   pyttsx3

    *   https://pypi.org/project/pyttsx3/

    *   https://github.com/nateshmbhat/pyttsx3

    *   https://pyttsx3.readthedocs.org

    ```shell
    pip install pyttsx3
    ```

    ```python
    import pyttsx3
    engine = pyttsx3.init() # object creation

    # RATE
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        # printing current voice rate
    engine.setProperty('rate', 125)     # setting up new voice rate

    # VOLUME
    volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
    print (volume)                          # printing current volume level
    engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1

    # VOICE
    voices = engine.getProperty('voices')       # getting details of current voice
    #engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

    engine.say("Hello World!")
    engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()
    engine.stop()

    # Saving Voice to a file
    # On Linux, make sure that 'espeak-ng' is installed
    engine.save_to_file('Hello World', 'test.mp3')
    engine.runAndWait()
    ```

    *   https://srivastavayushmaan1347.medium.com/getting-started-with-python-text-to-speech-a-beginners-guide-to-pyttsx3-a105f130c420

    *   https://dev.to/mr_nova/text-to-speech-with-python-a-beginners-guide-to-pyttsx3-2pie

*   gTTS

    *   https://pypi.org/project/gTTS/

    ```shell
    pip install gTTS
    ```

    *   https://www.geeksforgeeks.org/python/convert-text-speech-python/

*   TTS

    *   https://github.com/coqui-ai/TTS

    ```shell
    pip install TTS
    ```

*   pyt2s

    *   https://github.com/supersu-man/pyt2s

    ```shell
    pip install pyt2s
    ```

*   yapper-tts

    *   https://github.com/n1teshy/yapper-tts

*   python-espeak

    *   https://launchpad.net/python-espeak
    
    from espeak import espeak
    espeak.synth("Hello world.")

*   pypiwin32

*   pyTTS

    https://sourceforge.net/projects/uncassist/files/

*   smallest

    *   https://github.com/smallest-inc/smallest-python-sdk

    * needs API key => online

pyttsx

    https://pypi.org/project/pyttsx/
    pip install pyttsx
    https://github.com/RapidWareTech/pyttsx

## Diverse

*   https://www.reddit.com/r/learnpython/comments/18mubuv/what_are_some_of_great_text_to_speech_libraries/

*   https://stackoverflow.com/questions/1614059/how-to-make-python-speak

*   https://speechify.com/blog/text-to-speech-python/


https://github.com/calmoev01/first_assistant/commit/3a8f85e74182756566a18c937c7049de9b2d9a75

https://stackoverflow.com/questions/45347298/gtts-with-python-not-working
