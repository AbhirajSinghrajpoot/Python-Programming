import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(146, 177, 153), (49, 38, 45), (162, 144, 157), (168, 153, 43), (155, 176, 193), (81, 147, 128), (54, 123, 93), (229, 223, 224), (146, 17, 20), (74, 26, 20), (193, 164, 128), (196, 92, 74), (56, 94, 121), (107, 128, 154), (211, 219, 223), (154, 74, 53), (20, 55, 72), (137, 16, 10), (10, 95, 67), (167, 100, 103), (229, 176, 166), (183, 204, 172), (9, 66, 59), (18, 86, 89), (26, 68, 102), (104, 92, 94), (211, 205, 156)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()