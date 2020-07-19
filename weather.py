import time
import requests
import pyttsx3


# pyttsx3 config
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


print()
speak('Welcome to the Weather.')


def weather():
    api_key = '28c2103624ed3df9e6093bb50632748b'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak('Please enter a city below of which you want to see the weather of.')
    city_name = input("Enter city name : \n >>> ")
    print()
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

        print(' Temperature (in celsius unit) = ' + str(current_temperature - 273)[0:5] +
              '\n Temperature (in fahrenheit unit) = ' + str((current_temperature - 273) * 9/5 + 32)[0:5] +
              '\n Temperature (in kelvin unit) = ' + str(current_temperature)[0:5] +
              '\n Atmospheric pressure (in hPa unit) = ' + str(current_pressure) +
              '\n Humidity (in percentage) = ' + str(current_humidity) +
              '\n Description = ' + str(weather_description))

    else:
        print('City Not Found. Please try again.')


weather()
print()
time.sleep(3)
speak('You are now being redirected to the main file.')
print()
