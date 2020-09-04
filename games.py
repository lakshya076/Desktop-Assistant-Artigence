from datetime import datetime

from PySide2.QtCore import QRect
from PySide2.QtGui import QColor, QFont, QPalette, QCursor, Qt, QIcon
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QMenuBar, QMenu, QMainWindow


def pong():
    import pong


def tictactoe():
    import tic_tac_toe


def snake():
    import snake


def connect_four():
    import connect_four


class GameHub(QMainWindow):
    def __init__(self):
        super(GameHub, self).__init__()
        self.setGeometry(90, 50, 524, 186)
        self.setMinimumSize(524, 186)
        self.setMaximumSize(524, 186)
        self.setWindowIcon(QIcon('arti.PNG'))
        self.setWindowTitle('GameHub')

        palette = QPalette()
        palette.setColor(palette.Window, QColor('#000000'))
        palette.setColor(palette.WindowText, QColor('#FFFFFF'))
        palette.setColor(palette.Button, QColor("#00FF00"))
        palette.setColor(palette.ButtonText, QColor("#000000"))
        self.setPalette(palette)

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(0, 0, 682, 21)
        self.menubar.setFont(QFont('Roboto', 10))

        self.date_menu = QMenu(self.menubar)
        self.date_menu.setTitle(str(datetime.now().strftime('%d-%m-%Y')))

        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.date_menu.menuAction())

        self.label = QLabel(self)
        self.label.setGeometry(QRect(10, 30, 501, 51))
        self.label.setText("Hello, I am your host, Artigence. Welcome to GameHub. Please click on below buttons to "
                           "choose a game of your choice.")
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setFont(QFont('Roboto', 12))

        self.pong = QPushButton(self)
        self.pong.setGeometry(QRect(20, 130, 95, 33))
        self.pong.setCursor(QCursor(Qt.PointingHandCursor))
        self.pong.setText('Pong')

        self.tictactoe = QPushButton(self)
        self.tictactoe.setGeometry(150, 130, 95, 33)
        self.tictactoe.setCursor(QCursor(Qt.PointingHandCursor))
        self.tictactoe.setText('Tic-Tac-Toe')

        self.connect_four = QPushButton(self)
        self.connect_four.setGeometry(290, 130, 95, 33)
        self.connect_four.setCursor(QCursor(Qt.PointingHandCursor))
        self.connect_four.setText('Connect-4')

        self.snake = QPushButton(self)
        self.snake.setGeometry(420, 130, 95, 33)
        self.snake.setCursor(QCursor(Qt.PointingHandCursor))
        self.snake.setText('Snake')

        self.pong.clicked.connect(lambda: pong())
        self.tictactoe.clicked.connect(lambda: tictactoe())
        self.connect_four.clicked.connect(lambda: connect_four())
        self.snake.clicked.connect(lambda: snake())
