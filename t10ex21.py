def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l


def superposicio(l1, l2):
    for e in l1:
        if e in l2:
            return True
    return False


#Programa Principal: 
