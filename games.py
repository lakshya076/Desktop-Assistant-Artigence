import pyttsx3

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

print()
speak('Welcome to the GameHub. I am your host, Artigence.')
speak('We, at the moment have only two games namely: \n snake, \n pong.')
speak('Which one do you want to play?')


user_query = input(">>> ")

if 'snake' in user_query:
    speak('Opening Snake.')
    print()
    import snake

elif 'pong' in user_query:
    speak('Opening Pong.')
    print()
    import pong

print()
