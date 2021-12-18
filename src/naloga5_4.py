skrita_beseda=input("Vnesi skrito besedo: ")
izpis=skrita_beseda

for i in range (len(izpis)):
    izpis=izpis.replace(izpis[i],'_')

while True:
    crka = input("Vnesi črko: ")
    for i in range (len(skrita_beseda)):
        if skrita_beseda[i] == crka:
            izpis = list(izpis)
            izpis.pop(i)
            izpis.insert(i,crka)
            izpis = ''.join(izpis)
    if izpis==skrita_beseda:
        print(f'Bravo! Skrita beseda je: {izpis}')
        break
    print(izpis)