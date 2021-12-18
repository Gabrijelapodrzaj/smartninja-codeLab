from naloga7_2_zacetek import *

prva_stran()
odstevanje()
zacetek = time.time()


stevec = 0
def stej():
    global stevec
    stevec += 1


konc = 0
def koncaj():
    global konc
    konc += 1


turtle.onkeypress(stej, 'Return')
turtle.onkeypress(koncaj, 'k')
zaslon = turtle.Screen()
zaslon.listen()

hitrosti = naloga7_2_baza.preberi()
while True:
    time.sleep(1)
    turtle.clear()
    x = -100
    y = 100
    turtle.goto(x, y)
    turtle.write(f'Število pritiskov: {stevec}', font=('Ariel', 14, 'normal'))
    konec = time.time()
    cas = konec - zacetek
    hitrost = int(stevec / cas)
    x = -100
    y = -100
    turtle.goto(x, y)
    turtle.write(f'Pritiski na sekundo: {hitrost}', font=('Ariel', 14, 'normal'))
    turtle.speed(0)
    if hitrost > int(hitrosti[0]):
        hitrosti[4] = int(hitrosti[3])
        hitrosti[3] = int(hitrosti[2])
        hitrosti[2] = int(hitrosti[1])
        hitrosti[1] = int(hitrosti[0])
        hitrosti[0] = hitrost
    if konc == 1:
        break
naloga7_2_baza.zapisi(hitrosti)
