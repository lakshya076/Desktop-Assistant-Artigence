import pygame
import pyttsx3
from turtle import Turtle, Screen
from random import randint, choice
import turtle
print()

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
speak('Welcome to Pong.')

pygame.init()

ballspeed = 6
playerspeed = 50

cursor_size = 20
player_height = 60
player_width = 20

court_width = 1000
court_height = 600

FONT = ("Arial", 44, "normal")


def draw_border():
    border.pensize(3)
    border.penup()
    border.setposition(-court_width / 2, court_height / 2)
    border.pendown()
    border.forward(court_width)
    border.penup()
    border.sety(-court_height / 2)
    border.pendown()
    border.backward(court_width)


def filet():
    border.penup()
    border.pensize(1)
    border.setposition(0, -court_height / 2)
    border.setheading(90)
    border.pendown()

    for _ in range(court_height // 50):
        border.forward(50 / 2 + 1)
        border.penup()
        border.forward(50 / 2 + 1)
        border.pendown()


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    if y < court_height / 2 - player_height / 2:
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    if y > player_height / 2 - court_height / 2:
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    if y < court_height / 2 - player_height / 2:
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    if y > player_height / 2 - court_height / 2:
        paddle_b.sety(y)


def reset_ball():
    ball.setposition(0, 0)
    ball.setheading(choice([0, 180]) + randint(-60, 60))


def distance(t1, t2):
    my_distance = t1.distance(t2)

    if my_distance < player_height / 2:
        t2.setheading(180 - t2.heading())
        t2.forward(ballspeed)


# screen
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1.0, height=1.0)

# border
border = Turtle(visible=False)
border.speed('fastest')
border.color("white")

draw_border()
filet()

# Ball
ball = Turtle("circle")
ball.color("white")
ball.penup()
ball.speed("fastest")
reset_ball()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Player 1 score
score1 = 0
s1 = Turtle(visible=False)
s1.speed("fastest")
s1.color("white")
s1.penup()
s1.setposition(-court_width / 4, court_height / 3)
s1.write(score1, font=FONT)

# Player 2 score
score2 = 0
s2 = Turtle(visible=False)
s2.speed("fastest")
s2.color("white")
s2.penup()
s2.setposition(court_width / 4, court_height / 3)
s2.write(score2, font=FONT)


# Mainloop
def move():
    global score1, score2

    ball.forward(ballspeed)

    x, y = ball.position()

    if x > court_width / 2 + cursor_size:  # We define scoring
        score1 += 1
        s1.undo()
        s1.write(score1, font=FONT)
        reset_ball()
    elif x < cursor_size - court_width / 2:
        score2 += 1
        s2.undo()
        s2.write(score2, font=FONT)
        reset_ball()
    elif y > court_height / 2 - cursor_size or y < cursor_size - court_height / 2:
        # We define the border collision
        ball.setheading(-ball.heading())
    else:
        # Check collision between players and ball
        distance(paddle_a, ball)
        distance(paddle_b, ball)

    screen.ontimer(move, 20)


# Keyboard Bindings
screen.listen()
screen.onkeypress(paddle_a_up, 'w')
screen.onkeypress(paddle_a_down, 's')
screen.onkeypress(paddle_b_up, 'Up')
screen.onkeypress(paddle_b_down, 'Down')

# Restart
screen.onkey(reset_ball, "p")

screen.listen()

move()
screen.mainloop()
print()
