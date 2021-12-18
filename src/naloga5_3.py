besedilo=input("Vnesi besedilo: ")
tretja_beseda= input("Vnesi tretjo besedo: ")
def zamenjaj_3besedo (besedilo, tretja_beseda):
    besede =besedilo.split(" ")
    besede[2]= tretja_beseda
    besedilo= " ".join(besede)
    return besedilo
print(zamenjaj_3besedo(besedilo,tretja_beseda))