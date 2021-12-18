def izpis_matrike (matrika):
    for y in range (0,len(matrika),1):
        for x in range (0,len(matrika[y]),1):
            print(matrika[y][x], end=" ")
        print()
def pomnozi_matriko (matrika, st):
    for y in range (0,len(matrika),1):
        for x in range (0,len(matrika[y]),1):
            matrika[y][x]=matrika[y][x]*st
    return matrika
m= pomnozi_matriko([
    [1,2,3],
    [4,5,6],
    [7,8,9]
],3)
izpis_matrike(m)
