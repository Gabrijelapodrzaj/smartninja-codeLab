import random
stevec_uporabnik=0
stevec_racunalnik=0
while True:
    st_uporabnika = int(input("Vnesi število (0=škarje, 1=papir, 2=kamen): "))
    st_racunalnika = random.randint(0,2)
    print(f'Računalnik: {st_racunalnika}')
    if st_uporabnika==0 and st_racunalnika==1:
        stevec_uporabnik+=1
    if st_uporabnika==1 and st_racunalnika==2:
        stevec_uporabnik+=1
    if st_uporabnika==2 and st_racunalnika==0:
        stevec_uporabnik+=1
    if st_racunalnika==0 and st_uporabnika==1:
        stevec_racunalnik+=1
    if st_racunalnika==1 and st_uporabnika==2:
        stevec_racunalnik+=1
    if st_racunalnika==2 and st_uporabnika==0:
        stevec_racunalnik+=1
    if stevec_uporabnik==5:
        print("Uporabnik je zmagal.")
        break
    if stevec_racunalnik==5:
        print("Računalnik je zmagal.")
        break
