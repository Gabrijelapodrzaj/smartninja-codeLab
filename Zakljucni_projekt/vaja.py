import turtle
import time
stevec=0

def stej():
    global stevec
    stevec+=1

turtle.onkey(stej, 'k')
zaslon = turtle.Screen()
zaslon.listen()

while True:
    turtle.clear()
    turtle.write(stevec,font=('Monospace', 15, 'normal'))
    time.sleep(1)



