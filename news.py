from datetime import datetime
from PySide2.QtWidgets import QLabel, QPushButton, QMenuBar, QMenu, QMainWindow
from PySide2.QtGui import QIcon, QFont, QPalette, QColor, Qt
import requests
import pyttsx3

main_url = 'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=961d0075b7ca4ecdb5e8627658c18119'

open_bbc_page = requests.get(main_url).json()
article = open_bbc_page['articles']
results = []

for r in article:
    results.append(r['title'])


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 175)
    engine.say(audio)
    engine.runAndWait()


class News(QMainWindow):
    def __init__(self):
        super(News, self).__init__()

        self.setWindowTitle('News')
        self.setWindowIcon(QIcon('arti.PNG'))
        self.setGeometry(120, 100, 800, 600)
        self.setMaximumSize(800, 600)
        self.setMinimumSize(800, 600)
        self.setFont(QFont('Roboto', 12))

        palette = QPalette()
        palette.setColor(palette.Window, QColor('#000000'))
        palette.setColor(palette.WindowText, QColor('#FFFFFF'))
        self.setPalette(palette)

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(0, 0, 682, 21)
        self.menubar.setFont(QFont('Roboto', 10))

        self.date_menu = QMenu(self.menubar)
        self.date_menu.setTitle(str(datetime.now().strftime('%d-%m-%Y')))

        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.date_menu.menuAction())

        text = 'Welcome to News.\nThese are the latest international headlines according to BBC News Network.'

        heading = QLabel(self)
        heading.setText(text)
        heading.setGeometry(10, 30, 761, 81)
        heading.setAlignment(Qt.AlignHCenter)

        main_news = QLabel(self)
        main_news.setText(f'{str(results[0])}\n{str(results[1])}\n{str(results[2])}\n{str(results[3])}'
                          f'\n{str(results[4])}\n{str(results[5])}\n{str(results[6])}\n{str(results[7])}'
                          f'\n{str(results[8])}\n{str(results[9])}')
        main_news.setGeometry(10, 150, 761, 251)

        read = QLabel(self, text='Should I read it for you?')
        read.setGeometry(240, 490, 251, 41)

        button = QPushButton(self, text='Yes')
        button.setGeometry(500, 500, 131, 31)

        button.clicked.connect(lambda: self.on_click())

    def on_click(self):
        speak(f'{str(results[0])}\n{str(results[1])}\n{str(results[2])}\n{str(results[3])}'
              f'\n{str(results[4])}\n{str(results[5])}\n{str(results[6])}\n{str(results[7])}'
              f'\n{str(results[8])}\n{str(results[9])}')
