import turtle as t
import random

tim = t.Turtle()

colors = ["cornflowerblue", "darkorchid", "deeppink", "lightcoral", "mediumseagreen", "wheat", "slategray", "seashell2"]
direction = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

def random_walk(num_steps):
    for _ in range(num_steps):
        tim.color(random.choice(colors))
        tim.forward(50)
        tim.setheading(random.choice(direction))
        
random_walk(200)

screen = t.Screen()
screen.exitonclick()