from PySide2.QtCore import QRect, QSize, Qt
from PySide2.QtGui import QCursor, QFont, QIcon, QPalette, QColor, QKeySequence
from PySide2.QtWidgets import QPushButton, QLabel, QLineEdit, QApplication, QFrame, QMenu, QMenuBar, QMainWindow, \
    QAction
import pyttsx3
import wikipedia
import webbrowser
import os
import sys
import pyjokes
from datetime import datetime
import random
import wolframalpha


class Artigence(QMainWindow):
    def __init__(self):
        super(Artigence, self).__init__()

        # Basic Settings
        self.setGeometry(300, 200, 682, 422)
        self.setMinimumSize(QSize(682, 422))
        self.setMaximumSize(QSize(682, 422))
        self.setWindowIcon(QIcon("arti.PNG"))
        self.setWindowTitle("Artigence Home")

        # Color Scheme
        self.palette = QPalette()
        self.palette.setColor(self.palette.Window, QColor('#000000'))
        self.palette.setColor(self.palette.WindowText, QColor('#FFFFFF'))
        self.setPalette(self.palette)

        self.light_palette = QPalette()
        self.light_palette.setColor(self.light_palette.Window, QColor('#FFFFFF'))
        self.light_palette.setColor(self.light_palette.WindowText, QColor('#000000'))

        # Setting MenuBar
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(0, 0, 682, 21)

        self.date_menu = QMenu(self.menubar)
        self.date_menu.setTitle(str(datetime.now().strftime('%d-%m-%Y')))

        self.theme_menu = QMenu(self.menubar)
        self.theme_menu.setTitle('Theme')

        self.dark_theme = QAction('Dark Theme')
        self.dark_theme.setShortcut(QKeySequence('Ctrl+Shift+D'))
        self.theme_menu.addAction(self.dark_theme)
        self.dark_theme.triggered.connect(lambda: self.dark())

        self.light_theme = QAction('Light Theme')
        self.light_theme.setShortcut(QKeySequence('Ctrl+Shift+L'))
        self.theme_menu.addAction(self.light_theme)
        self.light_theme.triggered.connect(lambda: self.light())

        self.app_menu = QMenu(self.menubar)
        self.app_menu.setTitle('Apps')

        self.calculator_menu = QAction('Calculator')
        self.calculator_menu.setShortcut(QKeySequence('Alt+C'))
        self.app_menu.addAction(self.calculator_menu)
        self.calculator_menu.triggered.connect(lambda: self.calculator_func())

        self.game_menu = QAction('GameHub')
        self.game_menu.setShortcut(QKeySequence('Alt+G'))
        self.app_menu.addAction(self.game_menu)
        self.game_menu.triggered.connect(lambda: self.games_func())

        self.music_menu = QAction('Muse (Music)')
        self.music_menu.setShortcut(QKeySequence('Alt+M'))
        self.app_menu.addAction(self.music_menu)
        self.music_menu.triggered.connect(lambda: self.music_func())

        self.news_menu = QAction('News')
        self.news_menu.setShortcut(QKeySequence('Alt+E'))
        self.app_menu.addAction(self.news_menu)
        self.news_menu.triggered.connect(lambda: self.news_func())

        self.notepad_menu = QAction('Notepad')
        self.notepad_menu.setShortcut(QKeySequence('Alt+N'))
        self.app_menu.addAction(self.notepad_menu)
        self.notepad_menu.triggered.connect(lambda: self.notepad_func())

        self.pronunciator = QAction('Pronunciator')
        self.pronunciator.setShortcut(QKeySequence('Alt+P'))
        self.app_menu.addAction(self.pronunciator)
        self.pronunciator.triggered.connect(lambda: self.pronunciator_func())

        self.translate_menu = QAction('Translate')
        self.translate_menu.setShortcut(QKeySequence('Alt+T'))
        self.app_menu.addAction(self.translate_menu)
        self.translate_menu.triggered.connect(lambda: self.translate_func())

        self.weather_menu = QAction('Weather')
        self.weather_menu.setShortcut(QKeySequence('Alt+W'))
        self.app_menu.addAction(self.weather_menu)
        self.weather_menu.triggered.connect(lambda: self.weather_func())

        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.date_menu.menuAction())
        self.menubar.addAction(self.theme_menu.menuAction())
        self.menubar.addAction(self.app_menu.menuAction())

        # Creating Widgets
        self.query = QLineEdit(self)
        self.query.setGeometry(QRect(20, 30, 451, 41))
        self.query.setMinimumSize(QSize(451, 41))
        self.query.setMaximumSize(QSize(451, 41))
        self.query.setPlaceholderText("Enter your Query Here:")
        self.query.setFont(QFont('Roboto', 16))
        self.query.setClearButtonEnabled(True)

        self.update = QPushButton(self)
        self.update.setGeometry(QRect(491, 30, 171, 41))
        self.update.setMinimumSize(QSize(1, 1))
        self.update.setMaximumSize(QSize(171, 51))
        self.update.setText("What's New in the Updates?")
        self.update.setCursor(QCursor(Qt.PointingHandCursor))

        self.suggestions = QLabel(self)
        self.suggestions.setGeometry(QRect(20, 220, 111, 31))
        self.suggestions.setMinimumSize(QSize(111, 31))
        self.suggestions.setMaximumSize(QSize(111, 31))
        self.suggestions.setText("Suggestions:")
        self.suggestions.setFont(QFont('Roboto', 14))

        self.chrome = QPushButton(self)
        self.chrome.setGeometry(QRect(20, 260, 91, 31))
        self.chrome.setCursor(QCursor(Qt.PointingHandCursor))
        self.chrome.setText('Open Chrome')

        self.games = QPushButton(self)
        self.games.setGeometry(QRect(420, 260, 91, 31))
        self.games.setCursor(QCursor(Qt.PointingHandCursor))
        self.games.setText('Games')

        self.cmd = QPushButton(self)
        self.cmd.setGeometry(QRect(160, 260, 91, 31))
        self.cmd.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmd.setText('Open Cmd')

        self.joke = QPushButton(self)
        self.joke.setGeometry(QRect(160, 310, 91, 31))
        self.joke.setCursor(QCursor(Qt.PointingHandCursor))
        self.joke.setText('Joke Please!!')

        self.music = QPushButton(self)
        self.music.setGeometry(QRect(290, 260, 91, 31))
        self.music.setCursor(QCursor(Qt.PointingHandCursor))
        self.music.setText('Music')

        self.youtube = QPushButton(self)
        self.youtube.setGeometry(QRect(290, 310, 91, 31))
        self.youtube.setCursor(QCursor(Qt.PointingHandCursor))
        self.youtube.setText('Youtube')

        self.time = QPushButton(self)
        self.time.setGeometry(QRect(20, 310, 91, 31))
        self.time.setCursor(QCursor(Qt.PointingHandCursor))
        self.time.setText('Tell Time')

        self.weather = QPushButton(self)
        self.weather.setGeometry(QRect(420, 310, 91, 31))
        self.weather.setCursor(QCursor(Qt.PointingHandCursor))
        self.weather.setText('Weather')

        self.calculator = QPushButton(self)
        self.calculator.setGeometry(QRect(550, 260, 101, 31))
        self.calculator.setCursor(QCursor(Qt.PointingHandCursor))
        self.calculator.setText('Calculator')

        self.wikipedia = QPushButton(self)
        self.wikipedia.setGeometry(QRect(550, 310, 101, 31))
        self.wikipedia.setCursor(QCursor(Qt.PointingHandCursor))
        self.wikipedia.setText('India Wikipedia')

        self.news = QPushButton(self)
        self.news.setGeometry(QRect(20, 360, 91, 31))
        self.news.setCursor(QCursor(Qt.PointingHandCursor))
        self.news.setText('Latest News')

        self.meaning = QPushButton(self)
        self.meaning.setGeometry(QRect(420, 360, 231, 31))
        self.meaning.setCursor(QCursor(Qt.PointingHandCursor))
        self.meaning.setText('Meaning of Obsolete (or any word)')

        self.harry_potter = QPushButton(self)
        self.harry_potter.setGeometry(QRect(290, 360, 91, 31))
        self.harry_potter.setCursor(QCursor(Qt.PointingHandCursor))
        self.harry_potter.setText('Harry Potter')

        self.translate = QPushButton(self)
        self.translate.setGeometry(QRect(160, 360, 91, 31))
        self.translate.setCursor(QCursor(Qt.PointingHandCursor))
        self.translate.setText('Open Translate')

        self.line = QFrame(self)
        self.line.setGeometry(QRect(20, 200, 661, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.label = QLabel(self)
        self.label.setGeometry(QRect(20, 100, 631, 91))
        self.label.setFont(QFont('Roboto', 12))
        self.label.setTextFormat(Qt.AutoText)
        self.label.setWordWrap(True)

        self.wish()

        # Making the Widgets Functional
        self.query.returnPressed.connect(lambda: self.on_enter())
        self.query.returnPressed.connect(lambda: self.clear_text())

        self.update.clicked.connect(lambda: self.update_func())
        self.music.clicked.connect(lambda: self.music_func())
        self.games.clicked.connect(lambda: self.games_func())
        self.calculator.clicked.connect(lambda: self.calculator_func())
        self.weather.clicked.connect(lambda: self.weather_func())
        self.news.clicked.connect(lambda: self.news_func())
        self.translate.clicked.connect(lambda: self.translate_func())
        self.time.clicked.connect(lambda: self.time_func())
        self.joke.clicked.connect(lambda: self.joke_func())
        self.youtube.clicked.connect(lambda: self.youtube_func())
        self.wikipedia.clicked.connect(lambda: self.wikipedia_func())
        self.chrome.clicked.connect(lambda: self.chrome_func())
        self.cmd.clicked.connect(lambda: self.cmd_func())
        self.meaning.clicked.connect(lambda: self.meaning_func())
        self.harry_potter.clicked.connect(lambda: self.potter_func())

    def pronunciator_func(self):
        self.speak('Opening Pronunciator')
        from pronunciator import Pronunciator
        self.pronunciator_win = Pronunciator()
        self.pronunciator_win.show()

    def pong_func(self):
        import pong

    def notepad_func(self):
        self.speak('Opening Notepad')
        from notepad import Notepad
        self.notepad_win = Notepad()
        self.notepad_win.show()

    def update_func(self):
        os.startfile('Each Version Updates.txt')

    def translate_func(self):
        self.speak('Opening Translate\nPlease Wait as opening Translate may take up to 4-5 seconds')
        from translate import Translate
        self.translate_win = Translate()
        self.translate_win.show()

    def games_func(self):
        self.speak('Opening GameHub')
        from games import GameHub
        self.game_win = GameHub()
        self.game_win.show()

    def weather_func(self):
        self.speak('Opening Weather.')
        from weather import Weather
        self.weather_win = Weather()
        self.weather_win.show()

    def music_func(self):
        self.speak('Opening Muse')
        from music import Music
        self.music_win = Music()
        self.music_win.show()

    def calculator_func(self):
        self.speak('Opening Calculator.')
        from calculator import Calculator
        self.calculator_win = Calculator()
        self.calculator_win.show()

    def news_func(self):
        self.speak('Opening News.')
        from news import News
        self.news_win = News()
        self.news_win.show()
        self.speak('Welcome to News.\nThese are the latest international headlines according to BBC News Network.')

    def chrome_func(self):
        try:
            chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chrome_path)
            self.speak('Opening Chrome.')
        except Exception:
            self.speak('No Google Chrome installation found on the host device.')

    def cmd_func(self):
        cmd_path = 'C:\\Windows\\system32\\cmd.exe'
        os.startfile(cmd_path)
        self.speak('Opening Command Prompt.')

    def time_func(self):
        question = 'time'
        app_id = 'LLQ4QY-A7K3LEL4T8'
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        self.speak(answer)

    def joke_func(self):
        self.speak(pyjokes.get_joke())

    def youtube_func(self):
        webbrowser.open('https://www.youtube.com')
        self.speak('Opening Youtube.')

    def wikipedia_func(self):
        try:
            self.speak('Searching Wikipedia. Please Wait...')
            query = 'India'.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=1)
            self.speak('According to Wikipedia...')
            self.speak(result)
        except Exception as e:
            self.speak(e)

    def meaning_func(self):
        question = 'obsolete'
        app_id = 'LLQ4QY-A7K3LEL4T8'
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        self.speak(answer)

    def potter_func(self):
        new = 2
        google_url = "http://google.com/?#q="
        webbrowser.open(google_url + 'Harry Potter', new=new)

    def clear_text(self):
        self.query.clear()

    def on_enter(self):
        user_query = self.query.text().lower()

        if 'wikipedia' in user_query:
            try:
                self.speak('Searching Wikipedia. Please Wait...')
                user_query = user_query.replace('wikipedia', '')
                result = wikipedia.summary(user_query, sentences=1)
                self.speak('According to Wikipedia...')
                self.speak(result)
            except Exception as e:
                self.speak('Please try again later.')
                self.speak(e)

        elif 'youtube' in user_query:
            webbrowser.open('https://www.youtube.com')
            self.speak('Opening Youtube.')

        elif 'google' in user_query:
            webbrowser.open('https://www.google.com/')
            self.speak('Opening Google.')

        elif 'chrome' in user_query:  # You'll have to download google chrome first on your desktop/pc.
            try:
                chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
                os.startfile(chrome_path)
                self.speak('Opening Chrome')
            except Exception:
                self.speak('No Google Chrome installation found on the host device.')

        elif 'cmd' in user_query:
            cmd_path = 'C:\\Windows\\system32\\cmd.exe'
            os.startfile(cmd_path)
            self.speak('Opening Command Prompt.')

        elif 'control panel' in user_query:

            cp_path = 'C:\\Windows\\system32\\control.exe'
            os.startfile(cp_path)
            self.speak('Opening Control Panel.')

        elif 'bye' in user_query or 'goodbye' in user_query or 'good night' in user_query or 'see you later' in user_query:
            self.speak(random.choice(self.bye))
            sys.exit()

        elif 'hello' in user_query or 'hi' in user_query:
            self.speak(random.choice(self.hello))

        elif 'joke' in user_query:
            self.speak(pyjokes.get_joke())

        elif 'who are you' in user_query:
            self.speak('I am Artigence, your artificial intelligence.')

        elif 'map' in user_query or 'maps' in user_query:
            self.speak('Opening Google Maps.')
            webbrowser.open("https://www.google.com/maps")

        elif 'open calculator' in user_query or 'calculator' in user_query:
            self.calculator_func()

        elif 'news' in user_query:
            self.news_func()
            self.speak('Welcome to News.\nThese are the latest international headlines according to BBC News Network.')

        elif 'weather' in user_query:
            self.weather_func()

        elif 'games' in user_query:
            self.games_func()

        elif 'pronunciator' in user_query or 'pronounce' in user_query:
            self.pronunciator_func()

        elif 'translate' in user_query:
            self.translate_func()

        elif 'music' in user_query:
            self.music_func()

        elif 'notepad' in user_query:
            self.notepad_func()

        else:
            try:
                question = user_query
                app_id = 'LLQ4QY-A7K3LEL4T8'
                client = wolframalpha.Client(app_id)
                res = client.query(question)
                answer = next(res.results).text
                self.label.setText(answer)
                self.label.adjustSize()

            except:
                new = 2
                google_url = "http://google.com/?#q="
                query = user_query
                webbrowser.open(google_url + query, new=new)


    # The A.I. will speak through this function
    def speak(self, audio):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 165)
        self.label.setText(audio)
        self.engine.say(audio)
        self.engine.runAndWait()
        self.label.clear()

    def wish(self):
        hour = int(datetime.now().hour)
        if 0 <= hour < 12:
            self.speak('Good Morning.')
        elif 12 <= hour < 18:
            self.speak('Good Afternoon.')
        else:
            self.speak('Good Evening.')

        self.speak('I am Artigence.')
        self.speak('How may I help you today')

    hello = ['Kon\'nichiwa', 'Ciao', 'Hola', 'Bonjour', 'Hello', 'Hi', 'Hiya']
    bye = ['Adios', 'Goodbye', 'Bye-Bye', 'See you next time.', 'Artigence Out.',
           'It was nice talking to you sir. Have a nice day.']

    def dark(self):
        self.setPalette(self.palette)

    def light(self):
        self.setPalette(self.light_palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = Artigence()
    main_win.show()
    sys.exit(app.exec_())
