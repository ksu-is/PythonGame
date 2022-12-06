import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0)

snake = turtle.Turtle()
snake.shape("square")
snake.color("brown")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, -250)
pen.write("Score : 0 High Score : 0", align="center", font = 10)


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
	for index in range(len(Bodyplus)-1, 0, -1):
		x = Bodyplus[index-1].xcor()
		y = Bodyplus[index-1].ycor()
		Bodyplus[index].goto(x, y)
	if len(Bodyplus) > 0:
		x = snake.xcor()
		y = snake.ycor()
		Bodyplus[0].goto(x, y)
	move()
	for Body in Bodyplus:
		if Body.distance(snake) < 20:
			time.sleep(1)
			snake.goto(0, 0)
			snake.direction = "stop"
			for Body in Bodyplus:
				Body.goto(1000, 1000)
			Body.clear()

			score = 0
			delay = 0.1
			pen.clear()
			pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font = 10)
	time.sleep(delay)

window.mainloop()
