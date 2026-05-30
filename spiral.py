import turtle

t = turtle.Turtle()

s = turtle.Screen()

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

s.bgcolor('black')

t.speed('fastest')

t.hideturtle()

for x in range(50):

    t.pencolor(colors[x % len(colors)])

    t.width(x/100 + 1)

    t.forward(x)

    t.left(59)

turtle.done()