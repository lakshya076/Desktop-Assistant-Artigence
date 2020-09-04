from datetime import datetime
from PySide2.QtWidgets import QLineEdit, QRadioButton, QPushButton, QLabel, QMenu, QMenuBar, QMainWindow
from PySide2.QtGui import QIcon, QFont, QColor, QPalette, QCursor, Qt
import pyttsx3
import webbrowser


class Music(QMainWindow):
    def __init__(self):
        super(Music, self).__init__()
        self.setGeometry(20, 50, 522, 175)
        self.setMinimumSize(522, 175)
        self.setMaximumSize(522, 175)
        self.setWindowTitle('Muse')
        self.setWindowIcon(QIcon('arti.PNG'))
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

        self.song = QLineEdit(self)
        self.song.setPlaceholderText('Enter the name of song you want to search for:')
        self.song.setGeometry(10, 30, 501, 31)

        self.spotify = QRadioButton(self)
        self.spotify.setText('Spotify')
        self.spotify.setGeometry(120, 80, 101, 21)

        self.gaana = QRadioButton(self)
        self.gaana.setText('Gaana')
        self.gaana.setGeometry(330, 80, 91, 21)

        self.search = QPushButton(self)
        self.search.setText('Search')
        self.search.setGeometry(380, 130, 121, 31)
        self.search.clicked.connect(lambda: self.on_click())
        self.search.setCursor(QCursor(Qt.PointingHandCursor))

        self.label = QLabel(self)
        self.label.setGeometry(10, 130, 341, 31)

    def on_click(self):
        self.song_search = self.song.text()

        if self.song.text():
            if self.spotify.isChecked():
                self.speak('Searching your song on Spotify.')

                spotify_url = 'https://open.spotify.com/search/'
                webbrowser.open(spotify_url + self.song_search)

            elif self.gaana.isChecked():
                self.speak('Searching your song on Gaana.')

                gaana_url = 'https://gaana.com/search/'
                webbrowser.open(gaana_url + self.song_search)

            else:
                self.speak('Please choose either Spotify or Gaana.')
        else:
            self.speak('Please type a song name first')

        self.song.clear()

    def speak(self, audio):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.engine.setProperty('rate', 165)

        self.engine.say(audio)
        self.label.setText(audio)
        self.engine.runAndWait()
