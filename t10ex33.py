def llegir_llista():
    l = []
    a = ""
    while a != ".":
        a = input("Introdueix un nom (o '.' per acabar): ")
        if a != ".":
            l.append(a)
    return l

def noms_comencen_per(l, c):
    m = []
    for e in l:
        if e[0].lower() == c.lower():  
    
    print("Els noms que comencen per {} són: {}".format(c,m))

# Programa principal
l = llegir_llista()
c = input("Introdueix una lletra per comprovar els noms que comencen per ella: ")

noms_comencen_per(l, c)