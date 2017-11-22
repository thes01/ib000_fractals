import turtle

# helper method
def turtle_shift(turtle, pos_delta, angle_delta):
    turtle.penup()
    new_x = turtle.pos()[0] - pos_delta[1]
    new_y = turtle.pos()[1] + pos_delta[0]

    turtle.setpos(new_x, new_y)
    turtle.right(90 + angle_delta)
    turtle.pendown()

def dc_from_beginning(turtle, level, dist = 10):
    start_pos = turtle.pos()
    start_angle = turtle.heading()

    if level > 1:
        dc_from_beginning(turtle, level - 1, dist)
    else:
        turtle.backward(dist)

    pos_delta = (turtle.pos()[0] - start_pos[0], turtle.pos()[1] - start_pos[1])
    angle_delta = turtle.heading() - start_angle

    dc_from_middle(turtle, pos_delta, angle_delta, level, dist)

def dc_from_middle(turtle, pos_delta, angle_delta, level, dist = 10):
    turtle_shift(turtle, pos_delta, angle_delta)

    if level > 1:
        dc_from_beginning(turtle, level - 1, dist)
    else:
        turtle.backward(dist)

    turtle.left(90)
    turtle_shift(turtle, pos_delta, angle_delta)


bob = turtle.Turtle()
bob.speed(0)
bob.left(180)
bob.hideturtle()
# bob._tracer(0,0)

dc_from_beginning(bob, 9, 10)

# turtle.update()
turtle.done()
