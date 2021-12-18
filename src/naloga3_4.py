stevec = 0
vsota=0
while True:
    st = int(input("Vnesite število: "))
    if st == 0:
        break
    vsota = vsota + st
    stevec = stevec + 1

povprecje = vsota/stevec
print(f"Povprečje vnešenih števil je: {povprecje}")