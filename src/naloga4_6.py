st=int(input("Vnesi število: "))
def fakulteta (st):
    fakulteta=1
    for i in range(st):
        fakulteta=fakulteta*(st-i)
    return fakulteta
print(f"Fakulteta vnešenega števila je: {fakulteta(st)}")

