from tkinter import font
from turtle import Turtle, Screen
import random as rand
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = (0, -280)
FINISH_LINE = 290

class Car():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = rand.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(rand.choice(COLORS))
            random_y = rand.randint(-270,270)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup() 
        self.setheading(90)
        self.goto(STARTING_POSITION) 

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
    
    def left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def reset(self):
        self.goto(STARTING_POSITION)

    def at_finish(self):
        if self.ycor() == FINISH_LINE:
            return True
        else:
            return False

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.cscore = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-300,250)
        self.update()

    def update(self):
        self.write(f"Level: {self.cscore}", align="left", font=("Courier", 24, "normal"))

    def win(self):
        self.clear() 
        self.cscore += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="left", font=("Courier", 24, "normal"))

player = Player()
car_manager = Car()
scoreboard = Score()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

end_game = True
while end_game:
    screen.update()
    time.sleep(0.1)

    car_manager.create()
    car_manager.move_cars()

    #if turtle hits a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            end_game = False
            scoreboard.game_over()

    # player gets to the other side
    if player.at_finish():
        player.reset()
        scoreboard.win()
        car_manager.increase_speed()

    

screen.exitonclick()