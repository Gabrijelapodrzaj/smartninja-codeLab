st=int(input("Vnesi število: "))
def pomnozi_matriko (matrika,st):
    for i in range(len(matrika)):
        for j in range (len(matrika[i])):
            print(f"{matrika[i][j]*st}",end=" ")
        print()
matrika=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
pomnozi_matriko(matrika,st)