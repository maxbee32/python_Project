import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('red')
'''code for triangle start'''
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.backward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
'''code for triangle ends'''

"""dashed line code start"""
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
"""dashed line code ends"""

"""drawing different shapes"""
# for _ in range(3):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(120)
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
# for _ in range(5):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(72)
# for _ in range(6):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(60)
# for _ in range(7):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(51.4)
# for _ in range(8):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(45)
# for _ in range(9):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(40)
# for _ in range(10):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(36)

"""drawing different shapes ends"""

''' Challenge 4 - Random Walk '''
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colours = (r, g, b)
#     return colours
#
#
# # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
# #            "SeaGreen"]
# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")
#
# for _ in range(200):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))
#
#
'''Make a spirograph'''
timmy_the_turtle.color('black')
timmy_the_turtle.pensize(1)
timmy_the_turtle.speed(60)

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours


for i in range(36):
    # for color in ('red', 'magenta', 'blue',
    #               'cyan', 'green', 'white',
    #               'yellow'):
    timmy_the_turtle.color(random_color())

    timmy_the_turtle.circle(100)

    timmy_the_turtle.left(10)

    timmy_the_turtle.hideturtle()
    

screen = Screen()
screen.exitonclick()
