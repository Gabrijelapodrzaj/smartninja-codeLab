import projekt_baza
from projekt_funkcije import *
import random

zaslon = turtle.Screen()
zaslon.bgpic('ozadje.png')
# turtle.fillcolor('white')

premakni(0, 100)
izpisi("Pozdravljeni! Pred vami je program hitrostnega tipkanja.")
premakni(0, 70)
time.sleep(1)
izpisi("Ko stisnete enter se vam bo prikazala prva latinska beseda,")
premakni(0, 50)
izpisi("ko jo natipkate spet pritisnite enter. :)")
premakni(0, 10)
time.sleep(1)
izpisi("Ko napišete vseh 10 besed, se vam prikaže rezultat. ")
time.sleep(1)
premakni(0, -20)
izpisi('Veliko sreče!')
besede = projekt_baza.preberi()

pravilne_besede = 0
napake = 0
stevec = 0
zacetek = time.time()


def enter():
    global besede, pravilne_besede, stevec, zacetek, napake
    while True:
        stevec += 1
        turtle.clear()
        st_besede = random.randint(0, 68)
        x = random.randint(-200, 200)
        y = random.randint(150, 200)
        premakni(x, y)
        izpisi(besede[st_besede])
        turtle.speed(0)
        vnos = turtle.textinput('vnos', 'beseda')
        konec = time.time()
        cas = konec - zacetek
        if vnos == besede[st_besede]:
            pravilne_besede += 1
        else:
            napake += 1
        if pravilne_besede == 10:
            break
    turtle.clear()
    premakni(0, 100)
    hitrost = int(pravilne_besede * 60 / cas)
    izpisi(f"Hitrost vašega tipkanja je: {hitrost} besed na minuto")
    premakni(0, 70)
    izpisi(f'Pravilne besede ste napisali v {cas} sekundah.')
    premakni(0, 40)
    izpisi(f'Napačno ste napisali toliko besed: {napake}')
    time.sleep(5)
    turtle.bye()


turtle.onkeypress(enter, 'Return')

zaslon.listen()
zaslon.mainloop()