import turtle
import time
koti = int(input("Število kotov: "))
kot = int(360 / koti)
dolzina = int(input("Dolžina stranice: "))
st_likov = int(input("Število likov: "))
premik = 360 / st_likov
zelva = turtle.Turtle()

for i in range(st_likov):
    turtle.left(premik)
    for j in range(koti):
        turtle.forward(dolzina)
        turtle.left(kot)
time.sleep(5)
