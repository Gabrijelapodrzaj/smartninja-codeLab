besedilo = input("Vnesi besedilo: ")
def prestej_besede (besedilo):
    st_besed = len(besedilo.split(" "))
    return st_besed
def st_povedi (besedilo):
    stevec = 0
    for i in range (len(besedilo)):
        if besedilo[i]=='.'or besedilo[i]=='?' or besedilo[i]=='!':
            stevec+=1
    return stevec
def st_crk (besedilo):
    stevec = 0
    for i in range (len(besedilo)):
        if 'a'<=besedilo[i]<='z' or 'A'<=besedilo[i]<='Z':
            stevec+=1
    return stevec
def st_znakov (besedilo):
    stevec=0
    for i in range (len(besedilo)):
        if not('a'<=besedilo[i]<='z' or 'A'<=besedilo[i]<='Z'):
            stevec+=1
    return stevec

print(f"Skupen seštevek je: {prestej_besede(besedilo)+st_povedi(besedilo)+st_crk(besedilo)+st_znakov(besedilo)}")
