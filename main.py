import pyttsx3
import wikipedia
import webbrowser
import os
import sys
import pyjokes
from tkinter.filedialog import askdirectory
from datetime import datetime, date
import random
import wolframalpha
import time
import pymongo
from re import search
import smtplib

os.system('color 6')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def speak_without_print(audio_which_will_not_be_printed):
    engine.say(audio_which_will_not_be_printed)
    engine.runAndWait()


def start():
    client = pymongo.MongoClient("mongodb+srv://user:craptoshower@python-interactive-ai-e.brsnc.mongodb.net/Profiles"
                                 "?retryWrites=true&w=majority")

    database = client.get_database('Profiles')
    records = database.Names_and_Passwords

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


    class LoginOrRegister:
        speak('Do you want to login or register?')
        print('Please type the text "login" or "register" below as per your requirements.')
        response = input('Login or Register: \n >>> ')

    class User:
        username = input('Enter Username \n >>> ')
        email = input('Enter Email Address \n >>> ')

        # Create the user object
        user = {
            "name": username,
            "email": email
        }

        def validate(self, email):
            if search(regex, email):
                speak("Email is Valid.")
            else:
                speak("Invalid Email. The program will end now. Restart the program and enter a valid email address.")
                sys.exit()

    email_receivers = []

    if LoginOrRegister.response.lower() == 'register':
        registration_name = User.username
        registration_mail = User.email

        class_email = User()
        speak('Validating Email Address.')
        User.validate(self=class_email, email=registration_mail)

        speak('Authenticating Username.')

        # Check for existing username
        if records.find_one({
            "name": registration_name,
            "email": registration_mail
        }):
            speak('Username or Email already in use. The program will end now. If you have already registered, please'
                  ' restart the program and login with appropriate credentials.')
            sys.exit()

        # Will register if username does not exist in database
        elif records.insert_one(User.user):
            speak('Registering...')
            speak('Registered successfully.')
            email_receivers.append(registration_mail)
            speak(
                'The program will end in 10 seconds. Till then please don\'t forcefully close the program. After '
                'closing,'
                ' Restart and login to enjoy my services.')
            print('P.S. Check your mail inbox.')


    elif LoginOrRegister.response.lower() == 'login':
        login_name = User.username
        login_email = User.email

        class_email = User()
        speak('Validating Email Address.')
        User.validate(self=class_email, email=login_email)

        user = records.find_one({
            "name": login_name,
            "email": login_email
        })

        speak('Authenticating Username.')
        time.sleep(1)

        if user:
            speak('Appropriate Credentials entered.')
            speak('You can proceed.')
        else:
            speak('Username or the Email incorrect.')
            speak('The program will end now.')
            sys.exit()

    else:
        speak('You have to login or register to enjoy my services.')
        speak('I am not joking, this program is linked with a database in the cloud.')
        speak('So, I can authenticate your ID, email and password.')
        speak('Since you did not login or register, the program will end.')
        speak('To use my services, restart the program and either login or register.')
        sys.exit()

    # Sending Welcome Email to the newly registered user.
    # Email Account
    email_sender_account = "bot.of.artigence@gmail.com"
    email_sender_password = "artigenceisgood"
    email_smtp_server = "smtp.gmail.com"
    email_smtp_port = 587

    # Email Content
    email_body = """Welcome to the Artigence Family.
    Recently, you registered for my services and that shall be provided to you. 
    We are the Artigence family and you are welcome here anytime. 
    Even if you forget us, we will never forget you.
    If you ever feel any issue with me or suspect that something is malfunctioning in me:
     Please send me an email on this address as soon as possible.
    Yours Sincerely, 
        Artigence and Team."""

    # login to email server
    server = smtplib.SMTP(email_smtp_server, email_smtp_port)
    server.starttls()
    server.login(email_sender_account, email_sender_password)

    server.sendmail(email_sender_account, User.email, email_body)

    # All emails sent, log out.
    server.quit()


# A.I. will wish according to the hour with 'wish' function
def wish():

    hour = int(datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning.')
    elif 12 <= hour < 18:
        speak('Good Afternoon.')
    else:
        speak('Good Evening.')

    speak('I am Artigence.')
    speak('How may I help you today?')
    print()
    speak('Now, you can type commands in any case (upper, lower or mixed case.)')
    print('Write your commands when you see this sign ">>> "')
    time.sleep(2)
    print()
    print('Suggestions: \n open chrome \n open cmd \n play music \n calculator \n play games \n tell me a joke \n '
          'what is the time \n open my photos \n what is the weather \n salman khan wikipedia '
          '\n open stack overflow \n what is the latest news \n meaning of obsolete (or any word) \n what is today\'s '
          'date \n open translate')
    print()


hello = ['Kon\'nichiwa', 'Ciao', 'Hola', 'Bonjour', 'Hello', 'Hi', 'Hiya']
bye = ['Adios', 'Goodbye', 'Bye-Bye', 'See you next time.', 'Artigence Out.',
       'It was nice talking to you sir. Have a nice day.']



if __name__ == '__main__':
    start()
    print()
    print('What is updated in Version 1.3.3 ???\nNow you have to login or register to enjoy Atrigence\'s services.\nAll'
          ' the profiles '
          'stored in database in the cloud. So every user is authenticated before he/she is logged in.\nCommand color '
          'changed.'
          '\nFlexible and dynamic typing {meaning now you can type in any case (lower case, upper case or mixed case)}'
          '\nMinor and major Bug Fixes.\nNo satellite connections required. Everything is saved on your device\nMusic '
          'flexibility (now you can play music on either your pc or on the web'
          'on Spotify or Gaana.\nNew feature in calculator: Now you can also calculate powers.\nNew Feature in Weather:'
          ' Now you can view weather in celsius and fahrenheit unit.')
    print()
    wish()
    while True:
        user_query = input('>>> ').lower()  # Takes user_query in any alphabetical case

        if 'wikipedia' in user_query:
            print()
            try:
                speak('Searching Wikipedia. Please Wait...')
                user_query = user_query.replace('wikipedia', '')
                result = wikipedia.summary(user_query, sentences=2)
                speak('According to Wikipedia...')
                speak(result)
            except Exception as e:
                speak('Please try again later.')
                speak(e)
            print()

        elif 'youtube' in user_query:
            print()
            webbrowser.open('https://www.youtube.com')
            speak('Youtube opened.')
            print()

        elif 'google' in user_query:
            print()
            webbrowser.open('https://www.google.com/')
            speak('Google opened.')
            print()

        elif 'stack overflow' in user_query:
            print()
            webbrowser.open('https://stackoverflow.com/')
            speak('Stack overflow opened.')
            print()

        elif 'music' in user_query:
            print()
            speak('Do you want to hear music on your device or on the web.')
            music_response = input('Type in web or pc in next line. \n >>> ').lower()

            if music_response == 'pc':
                speak('Please choose a directory from where the songs will be played.')
                music_dir = askdirectory()
                os.chdir(music_dir)
                songs = os.listdir(music_dir)
                speak('Playing your songs.')
                os.startfile(os.path.join(music_dir, songs[0]))

            elif music_response == 'web':
                speak('Do you want to play on Gaana or Spotify.')
                web_response = input('Please type in gaana or spotify in the next line. \n >>> ').lower()
                print()
                if web_response == 'gaana':
                    gaana_url = 'https://gaana.com/search/'

                    speak('Please search a song you want to play.')
                    gaana_search = input('Enter the name of song. \n >>> ').lower()

                    speak('Opening the song on Gaana.')
                    webbrowser.open(gaana_url + gaana_search)
                    speak('Now you can play your song')

                elif web_response == 'spotify':
                    spotify_url = 'https://open.spotify.com/search/'

                    speak('Please search a song you want to play.')
                    spotify_search = input('Enter the name of song. \n >>> ').lower()

                    speak('Opening the song on Spotify.')
                    webbrowser.open(spotify_url + spotify_search)
                    speak('Now you can play your song')
                else:
                    speak('Please check your spelling.')
                    print()
                    speak('Type "music" again to restart.')
            print()

        elif 'date' in user_query:
            print()
            date = date.today()
            speak(date)
            print()

        elif 'open chrome' in user_query:  # You'll have to download google chrome first on your desktop/pc.
            print()
            try:
                chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
                os.startfile(chrome_path)
                speak('Chrome opened.')
            except Exception:
                speak('No Google Chrome installation found on the host device.')

        elif 'open notepad' in user_query:
            print()
            notepad_path = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(notepad_path)
            speak('Notepad opened.')
            print()

        elif 'open cmd' in user_query:
            print()
            cmd_path = 'C:\\Windows\\system32\\cmd.exe'
            os.startfile(cmd_path)
            speak('Command Prompt opened.')
            print()

        elif 'open control panel' in user_query:
            print()
            cp_path = 'C:\\Windows\\system32\\control.exe'
            os.startfile(cp_path)
            speak('Control Panel opened.')
            print()

        elif 'bye' in user_query or 'goodbye' in user_query or 'good night' in user_query or 'see you later' in user_query:
            print()
            speak(random.choice(bye))
            sys.exit()

        elif 'hello' in user_query or 'hi' in user_query:
            print()
            speak(random.choice(hello))
            print()

        elif 'joke' in user_query:
            print()
            speak(pyjokes.get_joke())
            print()

        elif 'open calculator' in user_query or 'calculator' in user_query:
            print()
            speak('Opening Calculator.')
            print()
            import calculator

            print()

        elif 'news' in user_query:
            print()
            speak('Opening News.')
            print()
            import news

            print()

        elif 'weather' in user_query:
            print()
            speak('Opening Weather.')
            print()
            import weather

            print()

        elif 'games' in user_query:
            print()
            speak('Opening GameHub.')
            print()
            import games

            print()

        elif 'translate' in user_query:
            print()
            speak('Opening Translate.')
            print()
            import translate

            print()

        elif 'who are you' in user_query:
            print()
            speak('I am Artigence, your artificial intelligence.')
            print()

        elif 'map' in user_query or 'maps' in user_query:
            print()
            speak('Opening Google Maps.')
            webbrowser.open("https://www.google.com/maps")
            print()

        else:
            print()
            try:
                question = user_query
                app_id = 'LLQ4QY-A7K3LEL4T8'
                client = wolframalpha.Client(app_id)
                res = client.query(question)
                answer = next(res.results).text
                print(answer)

            except:
                new = 2
                google_url = "http://google.com/?#q="
                query = user_query
                webbrowser.open(google_url + query, new=new)

            print()
