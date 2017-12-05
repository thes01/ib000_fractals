""" Draws the dragon curve with turtle graphics """

import turtle


def turtle_shift(my_turtle, pos_delta, angle_delta):
    """ A helper method that shifts the turtle to the end of dragon curve without drawing a line """
    my_turtle.penup()
    new_x = my_turtle.pos()[0] - pos_delta[1]
    new_y = my_turtle.pos()[1] + pos_delta[0]

    my_turtle.setpos(new_x, new_y)
    my_turtle.right(90 + angle_delta)
    my_turtle.pendown()


def dc_from_beginning(my_turtle, level, dist=10):
    """ Draws one half from beginning and the other half from the end"""
    start_pos = my_turtle.pos()
    start_angle = my_turtle.heading()

    if level > 1:
        dc_from_beginning(my_turtle, level - 1, dist)
    else:
        my_turtle.forward(dist)

    pos_delta = (my_turtle.pos()[0] - start_pos[0], my_turtle.pos()[1] - start_pos[1])
    angle_delta = my_turtle.heading() - start_angle

    dc_from_end(my_turtle, pos_delta, angle_delta, level - 1, dist)


def dc_from_end(my_turtle, pos_delta, angle_delta, level, dist=10):
    """ Starts drawing the curve from end - Shifts to the end and then draws as from begin """
    turtle_shift(my_turtle, pos_delta, angle_delta)

    if level > 0:
        dc_from_beginning(my_turtle, level, dist)
    else:
        my_turtle.forward(dist)

    my_turtle.left(90)
    turtle_shift(my_turtle, pos_delta, angle_delta)

bob = turtle.Turtle()
bob.speed(0)
bob.left(180)
bob.hideturtle()
# bob._tracer(0, 0)

dc_from_beginning(bob, 13, 5)
turtle.done()
