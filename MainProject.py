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

turtle.done()
