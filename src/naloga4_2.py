besedilo = input("Vnesi besedilo: ")
def st_povedi (besedilo):
    stevec = 0
    for i in range (len(besedilo)):
        if besedilo[i]=='.'or besedilo[i]=='?' or besedilo[i]=='!':
            stevec+=1
    return stevec
print(f"Število povedi v besedilou je: {st_povedi(besedilo)}")