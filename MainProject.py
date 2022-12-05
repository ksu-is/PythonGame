import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
 
# Board for the game
window = turtle.Screen()
window.title("Python Game")
window.bgcolor('white')
window.setup(width=600, height=600)
window.tracer(0)

#Snake
snake = turtle.Turtle()
snake.shape = ('square')
snake.color = ('green')
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

#Apple
apple = turtle.Turtle()
apple.color("red")
apple.shape("circle")
apple.speed()
apple.penup()
apple.goto(0, 100)

#Score Board
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center",
		font=("ariel", 24, "bold"))

#Movement
def group(): 
    if snake.direction != "down":
        snake.direction = "up"

def movedown():
    if snake.direction != "up":
        snake.direction = "down"

def moveleft(): 
    if snake.direction != "right":
        snake.direction = "left"

def moveright():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+20)

window.listen()
window.onkeypress(group, "w")
window.onkeypress(group, "s")
window.onkeypress(group, "a")
window.onkeypress(group, "d")

turtle.done()
