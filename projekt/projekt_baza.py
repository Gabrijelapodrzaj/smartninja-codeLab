def preberi():
    baza=open('datoteka.txt', 'r')
    string=baza.read()
    vsebina= string.split(' ')
    return vsebina


def zapisi(spisek):
    baza=open('../src/baza.txt', 'w')
    spisek=' '.join(spisek)
    baza.write(spisek)