besedilo=input("Vnesi besedilo: ")
def st_crk (besedilo):
    stevec = 0
    for i in range (len(besedilo)):
        if 'a'<=besedilo[i]<='z' or 'A'<=besedilo[i]<='Z':
            stevec+=1
    return stevec
print(f"Število črk v besedilu je: {st_crk(besedilo)}")