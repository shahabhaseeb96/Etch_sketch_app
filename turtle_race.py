from turtle import Turtle, Screen
import random
race_on =False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? pick a color :")
color = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
y_postions = [-100,-70,-40,-10,20, 50]
all_turtle =[]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_postions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    race_on = True

while race_on:

    for turtle in all_turtle:
        if turtle.xcor()> 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you win, the {winning_color} turtle color")
            else:
                print(f"you lost, the {winning_color} turtle color")
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)




screen.exitonclick()

