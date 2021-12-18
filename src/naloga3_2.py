stevec = 0
while True:
    st = int(input("Vnesi število: "))
    if st > 0:
        stevec = stevec + 1
    if st == 0:
        break
print(f"Vseh pozitivnih števil je: {stevec}.")