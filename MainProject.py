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
pen.write("Score : 0 High Score : 0", align="center", font=10)

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
window.onkeypress(movedown, "s")
window.onkeypress(moveleft, "a")
window.onkeypress(moveright, "d")

Bodyplus = []

while True:
	window.update()
	if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
		time.sleep(1)
		snake.goto(0, 0)
		snake.direction = "Stop"
		for Body in Bodyplus:
			Body.goto(1000, 1000)
		Bodyplus.clear()
		score = 0
		delay = 0.1
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font = 10)
	if snake.distance(apple) < 20:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		apple.goto(x, y)

		growth = turtle.Turtle()
		growth.speed(0)
		growth.shape("circle")
		growth.color("brown")
		growth.penup()
		Bodyplus.append(growth)
		delay -= 0.002
		score += 10
		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font = 10)
