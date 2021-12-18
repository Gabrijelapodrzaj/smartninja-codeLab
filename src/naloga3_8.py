stranica = int(input("Vnesi dolžino stranice: "))
for i in range (stranica):
    for j in range (i+1):
        print("*",end="")
    print()