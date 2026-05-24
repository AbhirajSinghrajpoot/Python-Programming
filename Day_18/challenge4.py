import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return (r, g, b)


direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

def random_walk(num_steps):
    for _ in range(num_steps):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(direction))
        
random_walk(200)