import turtle
from random import randint

def do_tree(turtle, length: int, angle = 45, multiplier = 10):
    turtle.forward(length * multiplier)

    if length >= 1:
        turtle.left(angle)
        do_tree(turtle, length - 1, angle, multiplier)
        turtle.right(2 * angle)
        do_tree(turtle, length - 1, angle, multiplier)
        turtle.left(angle)

    turtle.backward(length * multiplier)

def do_randomised_tree(turtle, length: int, angle = 45, multiplier = 10):
    turtle.forward(length * multiplier)

    angle_shift = randint(-15,15)

    if length >= 1:
        turtle.left(angle + angle_shift)
        do_randomised_tree(turtle, length - 1, angle, multiplier)
        turtle.right(2 * (angle + angle_shift))
        do_randomised_tree(turtle, length - 1, angle, multiplier)
        turtle.left(angle + angle_shift)

    turtle.backward(length * multiplier)


bob = turtle.Turtle()
bob._tracer(0,0)
bob.speed(0)
bob.left(90)

do_randomised_tree(bob, 10, angle=20, multiplier = 5)

turtle.done()
