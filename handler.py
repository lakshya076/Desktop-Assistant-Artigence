import pyttsx3
import sys
import time

# pyttsx3 configuration
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


#  A.I. will speak through this 'speak' function
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

time.sleep(2)
print()
speak('The file you were currently in had some issues because you are in the CrashHandler file.')
speak('This file has only one objective, close the whole program.')
speak('Artigence Out.')
sys.exit()
