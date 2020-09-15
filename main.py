import sys
import webbrowser
from datetime import datetime
import time
import pyttsx3
import requests
from PySide2 import QtCore
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, QPalette, QColor, QKeySequence, Qt, QFont
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMenuBar, QMenu, QAction


def yes_func():
    webbrowser.open('https://artigencedesktop.wordpress.com/updates-download/')


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # Basic Settings
        self.setGeometry(300, 200, 591, 280)
        self.setMinimumSize(QSize(591, 280))
        self.setMaximumSize(QSize(591, 280))
        self.setWindowIcon(QIcon("arti.PNG"))
        self.setWindowTitle("Artigence Updates")
        self.setFont(QFont('Roboto', 12))

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
        self.menubar.setFont(QFont('Roboto', 10))

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

        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.date_menu.menuAction())
        self.menubar.addAction(self.theme_menu.menuAction())

        # Widgets

        self.update_label = QLabel(self)
        self.update_label.setGeometry(20, 30, 551, 41)
        self.update_label.setText('Update Checker')
        self.update_label.setAlignment(Qt.AlignCenter)

        self.available = QLabel(self)
        self.available.setGeometry(20, 110, 541, 61)
        self.available.setText('')
        self.available.setAlignment(Qt.AlignCenter)

        self.yes = QPushButton(self)
        self.yes.setGeometry(350, 230, 75, 33)
        self.yes.setText('Yes')

        self.no = QPushButton(self)
        self.no.setGeometry(440, 230, 145, 33)
        self.no.setText('Just Open My App')

        self.no.clicked.connect(lambda: self.main_func())

    def main_func(self):
        self.setWindowFlags(QtCore.Qt.Tool)
        time.sleep(2)
        from start import Artigence
        self.main = Artigence()
        self.main.show()



    def dark(self):
        self.setPalette(self.palette)

    def light(self):
        self.setPalette(self.light_palette)

    # The A.I. will speak through this function
    def speak(self, audio):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 165)
        self.available.setText(audio)
        self.engine.say(audio)
        self.engine.runAndWait()
        self.available.clear()


if __name__ == '__main__':
    app = QApplication()
    win = Main()
    win.show()

    url = 'https://raw.githubusercontent.com/Lakshya-Saxena560/um/master/up.txt'
    req = requests.get(url)
    versions = req.text

    if versions[-6:-1] != '1.4.2':
        win.speak('A new version is available, Do you want to download it now?')
        win.yes.clicked.connect(lambda: yes_func())
    else:
        win.yes.setDisabled(True)
        win.speak('No updates available.')
        win.main_func()

    sys.exit(app.exec_())
