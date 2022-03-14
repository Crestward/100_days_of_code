from tkinter import font
from turtle import Turtle, Screen
import random as rand
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_postions = [(0,0), (-20,0), (-40,0)]
move_distance = 15
up = 90
down = 270
left = 180
right = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_postions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
 
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
   
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        random_x = rand.randint(-280, 280)
        random_y = rand.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = rand.randint(-280, 280)
        random_y = rand.randint(-280, 280)
        self.goto(random_x, random_y)
       
 
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()

    def read_highscore(self):
        with open("17_snake_highscore_data.txt", 'r') as txt:
            return int(txt.read())
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Arial",24,"normal"))

    def increase_score(self):
        self.score += 1  
        self.clear()    
        self.update_score()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("17_snake_highscore_data.txt", 'w') as txt:
            txt.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Arial",24,"normal"))
     

snake = Snake()
food = Food()
scoreboard = Score()

snake.create_snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


end_game = True
while end_game:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset()
        food.refresh()

    #if head collides with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset_score()
            snake.reset()
            food.refresh()

screen.exitonclick()