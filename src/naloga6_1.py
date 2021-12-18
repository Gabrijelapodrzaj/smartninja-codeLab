import time


def stevilo_besed(besedilo):
    besedilo = besedilo.split(' ')
    stevec = 0
    for i in range(len(besedilo)):
        stevec += 1

    return stevec

input("Pritisni enter za začetek.")
zacetek=time.time()
besedilo = input("Vnesi besedilo: ")
konec=time.time()

cas_pisanja= konec-zacetek

st_na_min= int(stevilo_besed(besedilo)*60/cas_pisanja)
print(f"Število besed na minuto: {st_na_min}")
