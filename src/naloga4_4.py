besedilo=input("Vnesi besedilo: ")
def st_znakov (besedilo):
    stevec=0
    for i in range (len(besedilo)):
        if not('a'<=besedilo[i]<='z' or 'A'<=besedilo[i]<='Z'):
            stevec+=1
    return stevec

print(f"Število znakov v besedilu je: {st_znakov(besedilo)}")