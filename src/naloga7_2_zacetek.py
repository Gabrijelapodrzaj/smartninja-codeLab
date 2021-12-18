import turtle
import time
from src import naloga7_2_baza


def odstevanje():
    turtle.clear()
    for i in range(0, 3):
        st = 3 - i
        x = 50 * i - 100
        y = 0
        turtle.hideturtle()
        turtle.up()
        turtle.goto(x, y)
        turtle.write(st, font=('Ariel', 14, 'normal'))
        time.sleep(1)
        if i==2:
            x=x+50
            turtle.goto(x,y)
            turtle.write('Start!!!',font=('Ariel', 14, 'normal'))

h= naloga7_2_baza.preberi()
def prva_stran():
    global h
    turtle.hideturtle()
    turtle.up()
    x=0
    y=50
    turtle.goto(x,y)
    turtle.write('enter=pritisk, k=konec', align='center', font=('Ariel', 14, 'normal'))
    x=0
    y=0
    turtle.goto(x,y)
    turtle.write('Najboljši rezultati: ',align='center', font=('Ariel', 14, 'normal'))
    for i in range (5):
        y=-30*(i+1)
        x=10
        turtle.goto(x,y)
        turtle.write(h[i], align='center',font=('Ariel', 14, 'normal'))
    time.sleep(3)
