import turtle
import random

turtle.pendown()


def left_move():
    turtle.left(90)
    turtle.forward(50)


def right_move():
    turtle.right(90)
    turtle.forward(50)


def back_move():
    turtle.right(180)
    turtle.forward(50)


def move():
    turtle.forward(50)


def restart():
    turtle.reset()


turtle.shape('turtle')

turtle.onkey(move, 'w')
turtle.onkey(right_move, 'd')
turtle.onkey(left_move, 'a')
turtle.onkey(back_move, 's')  
turtle.onkey(restart, 'Escape')
turtle.listen()
turtle.mainloop()
