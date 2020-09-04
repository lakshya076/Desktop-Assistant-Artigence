import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPalette, QColor
from PySide2.QtWidgets import QApplication, QComboBox, QFormLayout, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, \
    QSlider, QWidget
from PySide2.QtTextToSpeech import QTextToSpeech


class Pronunciator(QMainWindow):
    def __init__(self):
        super(Pronunciator, self).__init__()
        self.setMaximumHeight(21)
        self.setMinimumWidth(200)
        self.setWindowTitle('Pronunciator')
        self.setWindowIcon(QIcon('arti.PNG'))

        palette = QPalette()
        palette.setColor(palette.Window, QColor('#000000'))
        palette.setColor(palette.WindowText, QColor('#FFFFFF'))
        self.setPalette(palette)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QFormLayout(centralWidget)

        textLayout = QHBoxLayout()

        self.text = QLineEdit()
        self.text.setClearButtonEnabled(True)

        textLayout.addWidget(self.text)

        self.sayButton = QPushButton('Say')
        textLayout.addWidget(self.sayButton)

        self.text.returnPressed.connect(self.sayButton.animateClick)
        self.sayButton.clicked.connect(self.say)
        layout.addRow('Text:', textLayout)

        self.voiceCombo = QComboBox()
        layout.addRow('Voice:', self.voiceCombo)

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(100)
        layout.addRow('Volume:', self.volumeSlider)

        self.engine = None
        engineNames = QTextToSpeech.availableEngines()
        if len(engineNames) > 0:
            engineName = engineNames[0]
            self.engine = QTextToSpeech(engineName)
            self.engine.stateChanged.connect(self.stateChanged)

            self.voices = []
            for voice in self.engine.availableVoices():
                self.voices.append(voice)
                self.voiceCombo.addItem(voice.name())
        else:
            self.setWindowTitle('No voices available')
            self.sayButton.setEnabled(False)

    def say(self):
        self.sayButton.setEnabled(False)
        self.engine.setVoice(self.voices[self.voiceCombo.currentIndex()])
        self.engine.setVolume(float(self.volumeSlider.value()) / 100)
        self.engine.say(self.text.text())

    def stateChanged(self, state):
        if state == QTextToSpeech.State.Ready:
            self.sayButton.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = Pronunciator()
    mainWin.show()
    sys.exit(app.exec_())
