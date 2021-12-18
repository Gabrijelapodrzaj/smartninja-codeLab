vsota = 0
while True:
    st = int(input("Vnesi število: "))
    vsota = vsota + st
    if st==0:
        break
print(f"Vsota vnešenih števil je: {vsota}")