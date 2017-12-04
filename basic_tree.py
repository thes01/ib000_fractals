""" Basic tree fractal drawing script """

import turtle
from random import randint


def do_tree(my_turtle, length: int, angle=45, multiplier=10, max_randomise=0):
    """ Draw the tree """
    my_turtle.forward(length * multiplier)

    angle_shift = randint(-max_randomise, max_randomise)

    if length >= 1:
        my_turtle.left(angle)
        do_tree(my_turtle, length - 1, angle, multiplier, max_randomise)
        my_turtle.right(2 * (angle + angle_shift))
        do_tree(my_turtle, length - 1, angle, multiplier, max_randomise)
        my_turtle.left(angle + angle_shift)

    my_turtle.backward(length * multiplier)


foo = turtle.Turtle()
foo.speed(0)
foo.left(90)

do_tree(foo, 10, angle=20, multiplier=5)

turtle.done()
