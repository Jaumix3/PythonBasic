def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un nom: ")
        if a!=".":
            l.append(a)
    return l

def noms_comencen_per(l,c):
    m=[]
    for e in l:
        if e[-1]==c.upper() or e[-1]==c.lower():
            m.append(e)
    print("Els elements de la llista {} que comencen per {} són {}".format(l,c,m))

#Programa Princiapal
l = llegir_llista()
c = input("Introdeix un caràcter: ")
noms_comencen_per()