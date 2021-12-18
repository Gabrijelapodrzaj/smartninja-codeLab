import turtle
import time

def premakni(x,y):
    turtle.hideturtle()
    turtle.up()
    turtle.goto(x,y)
def izpisi(besedilo):
    turtle.write(besedilo,align='center',font=('Ariel', 14, 'normal'))
def odstevanje():
    for i in range(0, 3):
        st = 3 - i
        x = 50 * i - 100
        y = -20
        turtle.hideturtle()
        turtle.up()
        turtle.goto(x, y)
        turtle.write(st, font=('Ariel', 14, 'normal'))
        time.sleep(0.5)