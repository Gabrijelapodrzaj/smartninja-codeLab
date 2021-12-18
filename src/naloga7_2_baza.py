
def preberi():
    baza=open('baza.txt', 'r')
    string=baza.read()
    vsebina= string.split('\n')
    return vsebina


def zapisi(spisek):
    baza=open('baza.txt', 'w')
    spisek[0]=str(spisek[0])
    spisek[1]=str(spisek[1])
    spisek[2]=str(spisek[2])
    spisek[3]=str(spisek[3])
    spisek[4]=str(spisek[4])
    spisek='\n'.join(spisek)
    baza.write(spisek)
