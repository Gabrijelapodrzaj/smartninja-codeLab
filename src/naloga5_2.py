polje=[
    [".",".","."],
    [".",".","."],
    [".",".","."]
]
for i in range (9):
    x1 = int(input("Vnesi x koordinato: "))
    while 0 > x1 or x1 > 2:
        x1 = int(input("Koordinata je zunaj polja, ponovno vnesi koordinato x: "))

    y1 = int(input("Vnesi y koordinato: "))
    while 0 > y1 or y1 > 2:
        y1 = int(input("Koordinata je zunaj polja, ponovno vnesi koordinato y: "))

    while polje[y1][x1] != ".":
        print("Koordinati sta zasedeni, ponovno vnesi vrednosti.")
        x1 = int(input("Vnesi x koordinato: "))
        while 0 > x1 or x1 > 2:
            x1 = int(input("Koordinata je zunaj polja, ponovno vnesi koordinato x: "))
        y1 = int(input("Vnesi y koordinato: "))
        while 0 > y1 or y1 > 2:
            y1 = int(input("Koordinata je zunaj polja, ponovno vnesi koordinato y: "))

    polje[y1][x1] = "O"

    for i in range(len(polje)):
        for j in range(len(polje[i])):
            print(polje[i][j], end="")
        print()


    x2=int(input("Vnesi x koordinato: " ))
    while 0>x2 or x2>2:
        x2 = int(input("Koordinata je zunaj polja, ponovno vnesi koordinato x: "))
    y2=int(input("Vnesi y koordinato: " ))
    while 0>y2 or y2>2:
        y2 = int(input("Koordinata je zunaj polja, ponovno vnesi koordinato y: "))


    while polje[y2][x2] != ".":
        print("Koordinati sta zasedeni, ponovno vnesi vrednosti.")
        x2 = int(input("Vnesi x koordinato: "))
        while 0 > x2 or x2 > 2:
            x2 = int(input("Koordinata je zunaj polja, ponovno vnesi koordinato x: "))
        y2 = int(input("Vnesi y koordinato: "))
        while 0 > y2 or y2 > 2:
            y2 = int(input("Koordinata je zunaj polja, ponovno vnesi koordinato y: "))

    polje[y2][x2]="X"

    for i in range (len(polje)):
        for j in range (len(polje[i])):
            print(polje[i][j], end="")
        print()