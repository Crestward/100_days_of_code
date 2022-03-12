from tkinter import font
from turtle import Turtle, Screen
import random as rand
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)


class Paddle(Turtle):
    def __init__(self, cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup() 
        self.goto(cord)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.movement = 0.1

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos,y_pos)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.movement *= 0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.movement = 0.1
        self.bounce_x()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_win(self):
        self.clear() 
        self.l_score += 1
        self.update()

    def r_win(self):
        self.clear() 
        self.r_score += 1
        self.update()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))   
ball = Ball()
scoreboard  = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


end_game = True
while end_game:
    time.sleep(ball.movement)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    # paddle misses ball
    #right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_win()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_win()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        end_game = False
        print("Game over") 

screen.exitonclick()
