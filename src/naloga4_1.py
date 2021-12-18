besedilo = input("Vnesi besedilo: ")
def prestej_besede (besedilo):
    st_besed = len(besedilo.split(" "))
    return st_besed
print(f"Število besed v besedilu je: {prestej_besede(besedilo) }")