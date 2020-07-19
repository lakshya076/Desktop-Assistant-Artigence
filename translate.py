import os
from textblob import TextBlob
import pyttsx3
import random

os.system('color 6')

# pyttsx3 config
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

print()
speak('Welcome to Translate.')
print()


def translate():
    speak('Enter the text you want to print in the next line (The text should be in English):')
    text = input(">>> ")
    print()

    speak('This app only supports these languages:')
    print('French, German, Dutch, Spanish, Italian, Hindi, Portugese, Welsh')
    print()
    speak('Enter the language you want to print to in the next line. (in all small. For Example: french)')
    print()

    language = input('>>> ')

    translator = TextBlob(text)

    if language == 'french':
        france = translator.translate(to='fr')
        speak(france)

    elif language == 'german':
        germany = translator.translate(to='de')
        speak(germany)

    elif language == 'dutch':
        netherlands = translator.translate(to='nl')
        speak(netherlands)

    elif language == 'spanish':
        spain = translator.translate(to='es')
        speak(spain)

    elif language == 'italian':
        italy = translator.translate(from_lang='en', to='it')
        speak(italy)

    elif language == 'hindi':
        india = translator.translate(to='hi')
        print(india)

    elif language == 'portugese':
        brazil_and_portugal = translator.translate(to='pt')
        speak(brazil_and_portugal)

    elif language == 'welsh':
        welsh = translator.translate(to='cy')
        speak(welsh)

    else:
        speak('Invalid Input.')


translate()
print()
speak('You are being redirected to the main program.')
print()
