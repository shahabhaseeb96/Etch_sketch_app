from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()


def forward():
    timmy.forward(10)


def up():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def backword():
    timmy.backward(10)


def down():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def rest():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(fun=forward, key="d")
screen.onkey(fun=up, key="w")
screen.onkey(fun=backword,key="a")
screen.onkey(fun=down,key="s")
screen.onkey(fun=rest, key="c")
screen.exitonclick()

