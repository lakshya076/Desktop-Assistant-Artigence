from datetime import datetime

from PySide2.QtCore import QRect, QSize
from PySide2.QtGui import QFont, QIcon, QPalette, QColor
from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QMenuBar, QMenu, QMainWindow
import pyttsx3
import time
import requests


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 165)
    engine.say(audio)
    engine.runAndWait()


class Weather(QMainWindow):
    def __init__(self):
        super(Weather, self).__init__()

        self.resize(530, 414)
        self.setMinimumSize(QSize(530, 414))
        self.setMaximumSize(QSize(530, 414))
        self.setGeometry(800, 130, 530, 414)
        self.setFont(QFont('Roboto', 12))
        self.setWindowIcon(QIcon('arti.PNG'))
        self.setWindowTitle('Weather')

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

        self.city = QLineEdit(self)
        self.city.setObjectName(u"city")
        self.city.setGeometry(QRect(10, 30, 511, 41))
        self.city.setMinimumSize(QSize(511, 41))
        self.city.setMaximumSize(QSize(511, 41))
        self.city.setPlaceholderText('Enter the city name of which you want to view the weather.')
        self.city.setToolTip('Enter the city name of which you want to view the weather.')

        self.celsius = QLabel(self)
        self.celsius.setGeometry(QRect(10, 90, 491, 31))

        self.fahrenheit = QLabel(self)
        self.fahrenheit.setGeometry(QRect(10, 140, 491, 31))

        self.kelvin = QLabel(self)
        self.kelvin.setGeometry(QRect(10, 190, 491, 31))

        self.pressure = QLabel(self)
        self.pressure.setGeometry(QRect(10, 240, 491, 31))

        self.humidity = QLabel(self)
        self.humidity.setGeometry(QRect(10, 290, 491, 31))

        self.description = QLabel(self)
        self.description.setGeometry(QRect(10, 340, 491, 31))

        speak('Welcome to the Weather.')

        self.city.returnPressed.connect(lambda: self.weather())
        self.city.returnPressed.connect(lambda: self.clear_text())

    def clear_text(self):
        self.city.clear()

    def weather(self):
        api_key = '28c2103624ed3df9e6093bb50632748b'
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        city_name = self.city.text()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x['cod'] != '404':
            y = x['main']
            current_temperature = y['temp']
            current_pressure = y['pressure']
            current_humidity = y['humidity']
            z = x['weather']
            weather_description = z[0]['description']

            self.celsius.setText('Temperature (in celsius unit) = ' + str(current_temperature - 273)[0:5])
            time.sleep(0.5)
            self.fahrenheit.setText(
                'Temperature (in fahrenheit unit) = ' + str((current_temperature - 273) * 9 / 5 + 32)[0:5])
            time.sleep(0.5)
            self.kelvin.setText('Temperature (in kelvin unit) = ' + str(current_temperature)[0:5])
            time.sleep(0.5)
            self.pressure.setText('Atmospheric pressure (in hPa unit) = ' + str(current_pressure))
            time.sleep(0.5)
            self.humidity.setText('Humidity (in percentage) = ' + str(current_humidity))
            time.sleep(0.5)
            self.description.setText('Description = ' + str(weather_description))

        else:
            speak('City Not Found. Please try again.')
