import turtle as t
from random import randint


def equilateral_triangle():
    t.penup()
    t.setposition(0, 200)
    t.pendown()
    t.settiltangle()
    t.right(60)
    t.forward(200)
    t.right(120)
    t.forward(200)
    t.right(120)
    t.forward(200)
    t.hideturtle()
    t.exitonclick()


# Not quite working right... Work on this later. Probably best to just do it for one star
def create_star(points):
    t.penup()
    t.setposition(0, 200)
    t.pendown()
    t.colormode(255)
    internal_angle = ((points - 2) * 180) / points  # internal angle of equilateral shape inside star
    desired_angle = 180 - ((180 - internal_angle) * 2)  # angle of star points
    initial_right = 90 - (desired_angle / 2)  # turtle starts at 90 degrees so initial right will be different
    t.right(initial_right)
    if points % 2 != 0:
        for i in range(points):
            t.forward(200)
            t.right(180 - desired_angle)
            t.pencolor(randint(0, 255),
                       randint(0, 255),
                       randint(0, 255))
    else:
        for i in range(points // 2):
            t.forward(200)
            t.right(180 - desired_angle)
            t.pencolor(randint(0, 255),
                       randint(0, 255),
                       randint(0, 255))
        t.penup()
        t.setposition(0, -150)
        t.pendown()
        t.right(180)
        for i in range(points // 2):
            t.forward(200)
            t.right(180 - desired_angle)
            t.pencolor(randint(0, 255),
                       randint(0, 255),
                       randint(0, 255))

    t.hideturtle()
    t.exitonclick()


create_star(10)
