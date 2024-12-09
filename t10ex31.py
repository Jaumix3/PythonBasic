def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":
            l.append(a)
    return l

def mostrar_majors_que(t, min, max):
    for e in t:
        if e>num:
            print("{} és major que {}".fortmat(e,num))


#Programa Principal:
x = llegir_llista()
y = tuple(x)
num=int(input("Introdueixi el numero a comparar: "))
max=int(input())
