st1=float(input("Vnesi število: "))
def fakulteta (st2):
    fakulteta=1
    for i in range(st2):
        fakulteta=fakulteta*(st2-i)
    return fakulteta
def sinus (st3):
    sinus=0
    stevec=0
    for i in range (1,22,2):
        if stevec%2==0:
            sinus=sinus+(st3**i)/fakulteta(i)
            stevec+=1
        else:
            sinus=sinus-(st3**i)/fakulteta(i)
            stevec+=1
print(f"Sinus vnešenega števila je: {sinus(st1)}")
