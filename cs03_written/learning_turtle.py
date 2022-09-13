import turtle as t


def turtle_draw_rectangle():
    t.pencolor('red')
    t.forward(200)
    t.left(90)
    t.pencolor('blue')
    t.forward(150)
    t.left(90)
    t.pencolor("green")
    t.forward(200)
    t.left(90)
    t.pencolor('black')
    t.forward(150)
    t.hideturtle()
    t.exitonclick()


def turtle_draw_octogon():
    t.pencolor('red')
    t.penup()
    t.setposition(-45, 100)
    t.pendown()
    for i in range(8):
        t.forward(80)
        t.right(45)
    distance = 0.2
    angle = 40
    t.pencolor('blue')
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    for i in range(100):
        t.forward(distance)
        t.left(angle)
        distance += 0.5

    t.hideturtle()
    t.exitonclick()


def draw_triangle():
    t.penup()
    t.setposition(0, 200)
    t.right(60)
    t.pendown()
    t.forward(200)
    t.right(120)
    t.forward(200)
    t.right(120)
    t.forward(200)
    t.hideturtle()
    t.exitonclick()


def draw_star():
    t.speed(1)
    t.penup()
    t.setposition(0, 250)
    t.pendown()
    t.right(72)
    t.forward(300)
    for i in range(4):
        t.right(144)
        t.forward(300)

    t.hideturtle()
    t.exitonclick()


draw_star()
