from turtle import *
timmy_the_turtle = Turtle()


for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    
    
screen = Screen()
screen.exitonclick()