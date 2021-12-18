import turtle
import random

dtekst = open("../Zakljucni_projekt/datoteka.txt", "r")
tekst = dtekst.read()
spisek = tekst.split(' ')


def enter():
    turtle.clear()
    turtle.up()
    turtle.hideturtle()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    turtle.goto(x, y)
    turtle.write(spisek[random.randint(0, 68)], font=('Monospace', 15, 'normal'))
    turtle.speed(0)


enter()
screen = turtle.Screen()
screen.onkeypress(enter, 'Return')
screen.listen()
screen.mainloop()
