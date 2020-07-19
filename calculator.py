import pyttsx3
import random
import os

os.system('color 6')

#  pyttsx3 configuration
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


print()
speak('Welcome to the calculator.')


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def remainder(x, y):
    return x % y


def exponent(x, y):
    return x ** y


speak("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remainder")
print("6. Power")

print()
# Take input from the user
choice = input("Enter choice (1/2/3/4/5/6): \n >>>  ")

if choice in ('1', '2', '3', '4', '5'):
    num1 = float(input("Enter first number: \n >>> "))
    num2 = float(input("Enter second number: \n >>> "))

    if choice == '1':
        speak(add(num1, num2))

    elif choice == '2':
        speak((num1, num2))

    elif choice == '3':
        speak(multiply(num1, num2))

    elif choice == '4':
        speak(divide(num1, num2))

    elif choice == '5':
        speak(remainder(num1, num2))

    else:
        speak("Invalid Input")

elif choice == '6':
    number1 = float(input('Enter the number: \n >>> '))
    power = float(input('Enter to which power you want to multiply. \n >>> '))
    speak(exponent(number1, power))

print()
speak('You are now being redirected to the main file.')
print()
