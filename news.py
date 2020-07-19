import requests
import pyttsx3
import time
import os

os.system('color 6')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def speak_without_print(only_audio):
    engine.say(only_audio)
    engine.runAndWait()


try:
    print()
    speak('Welcome to News.')
    speak('These are the latest international headlines according to BBC News Network.')
    print()

    main_url = 'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=961d0075b7ca4ecdb5e8627658c18119'

    open_bbc_page = requests.get(main_url).json()
    article = open_bbc_page['articles']
    results = []

    for r in article:
        results.append(r['title'])

    for i in range(len(results)):
        print(str(i + 1) + '.', results[i])

    time.sleep(1)

    print()
    speak('Do you want me to read them for you ?')
    speak('Answer in yes or no.')
    response = input('Type the answer in the next line: \n >>> ')

    if response == 'yes':
        speak_without_print(results)
    else:
        speak('Fine.')
    print()

except Exception as e:
    speak('Please try again later. I regret the inconvenience.')

print()
speak('Now you are being redirected to the main file.')
print()
