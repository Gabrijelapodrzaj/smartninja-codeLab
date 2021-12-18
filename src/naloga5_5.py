polje=[
    ['.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.']
]
while True:
    while True:
        x1=int(input("Vnesi indeks stolpca: "))
        if x1<0 or x1>6:
            print('Vnešen indeks je zunaj igralnega polja.')
        else:
            break

    while True:
        y1 = 3
        if polje [y1][x1]=='.':
            break
        if polje[y1][x1]=='o' or polje[y1][x1]=='x':
            y1=2
        if polje[y1][x1]=='o' or polje[y1][x1]=='x':
            y1=1
        if polje[y1][x1]=='o' or polje[y1][x1]=='x':
            y1=0
        if polje [y1][x1]=='.':
            break
        if y1 == 0:
            x1 = int(input('Izbran stolpec je že poln. Ponovno vnesi x: '))


    polje[y1][x1]='x'

    for i in range(len(polje)):
        for j in range(len(polje[i])):
            print(polje[i][j], end="")
        print()

    while True:
        x2=int(input("Vnesi indeks stolpca: "))
        if x2<0 or x2>6:
            print('Vnešen indeks je zunaj igralnega polja.')
        else:
            break

    while True:
        y2 = 3
        if polje[y2][x2] == '.':
            break
        if polje[y2][x2] == 'o' or polje[y2][x2] == 'x':
            y2 = 2
        if polje[y2][x2] == 'o' or polje[y2][x2] == 'x':
            y2 = 1
        if polje[y2][x2] == 'o' or polje[y2][x2] == 'x':
            y2 = 0
        if polje[y2][x2] == '.':
            break
        if y2 == 0:
            x2 = int(input('Izbran stolpec je že poln. Ponovno vnesi o: '))
    polje[y2][x2]='o'

    for i in range(len(polje)):
        for j in range(len(polje[i])):
            print(polje[i][j], end="")
        print()

