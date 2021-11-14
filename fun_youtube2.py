import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(9)

for i in range(4):
    for colours in ["red","magenta","blue","cyan","green","yellow","white"]:
        turtle.color(colours)
        turtle.circle(80)
        turtle.left(12)
turtle.hideturtle()
