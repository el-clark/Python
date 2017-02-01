#!/usr/bin/env python3
import os
import re
import subprocess
import time # to do time.sleep(5) for debugging
# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
# obtain audio from the microphone
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

# recognize speech using Google Speech Recognition
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        if re.search('[Oo]pen [Ff]irefox', r.recognize_google(audio)):
           #os.system("firefox")
           FireFox = subprocess.Popen(["firefox"])
           Speak = subprocess.call(['espeak Firfox has been opened'], shell=True)
        elif re.search('[Cc]lose [Ff]irefox', r.recognize_google(audio)):
           #try:
              FireFox.terminate()
           #except Error:
           #   print("Firefox is not open stupid!")
        elif re.search('[Ee]xit', r.recognize_google(audio)):
           exit()
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
