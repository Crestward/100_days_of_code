from turtle import Turtle, Screen
import random as rand


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Pick a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
y_positions = [-70, -40, -10, 20, 50, 80]
for turtle in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.color(colours[turtle])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle])
    all_turtles.append(tim)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You lose. The {winning_color} turtle is the winner. The {user_bet} turtle lost")
        rand_distance = rand.randint(0,10)
        turtle.forward(rand_distance)
        

screen.exitonclick()