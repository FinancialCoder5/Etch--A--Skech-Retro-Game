from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    """Moves the Pointer ahead of the User"""
    tim.forward(10)


def move_backwards():
    """Moves the Location Backwards of the user"""
    tim.backward(10)


def move_left():
    """Location of the pointer to move towards right of the user"""
    tim.left(10)


def move_right():
    """Location of the pointer to move towards left """
    tim.right(10)


def clear():
    """This function is going to wipe out the screen while you press C """
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.exitonclick()
