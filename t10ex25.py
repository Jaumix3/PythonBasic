def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l
def gran_llista(l):
    return max(l)

#Programa Principal

a = llegir_llista()
print("El Major de la llista {} és {}".fortmat(a, gran_llista(a)))