import turtle
import time
st_kotov = int(input("Vnesi število kotov: "))
kot_premika = 360 / st_kotov
dolzina = int(input("Vnesi dolžino stranice: "))

zelva = turtle.Turtle()
for i in range(st_kotov):
    zelva.forward(dolzina)
    zelva.left(kot_premika)
    zelva.speed(1)
time.sleep(5)

