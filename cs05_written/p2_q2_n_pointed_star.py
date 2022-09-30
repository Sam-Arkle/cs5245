import math
import turtle as t


# Idea is, you'll have a circle. The star is drawn by connecting the points by skipping the next respective angle. o
# skips would construct a circle

def n_pointed_star(n, skips):
    t1 = t.Turtle()  # circle
    t2 = t.Turtle()  # drawer
    radius = 50
    angle = 360 / n
    t1.penup()
    t2.penup()
    t1.setposition(0, 100)
    t2.setposition(0, 100)
    t2.pendown()
    for i in range(n):
        t1.circle(-radius, (skips + 1) * angle)
        new_pos = t1.pos()
        t2.setposition(new_pos)

    t1.hideturtle()
    t2.hideturtle()
    t.exitonclick()


n_pointed_star(10, 2)
