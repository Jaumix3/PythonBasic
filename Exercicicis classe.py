"""def ex1():
a={1,2,3,4,5,6}
b= len(a)
if 2 in a:
    print("El 2 és dins a ")
else:
    print("El 2 no és dins a "
    a={"nom": "Jaume", "cognom": "Cardona", "Telf": "633263320"}
#for e in a:
  #  print("{} {}".format(e,a[e]))
for x,y in a.items():
    print(x,y)
a = {"e1":"v1", "e2":"v2", "e3":{"e3":"Pepe", "e32":"Ramis"}}
print(a.get("e3"))
print(a.items("e3"))
print(a.keys("e3"))
print(a.values("e3"))"

a={"contacte1":{"nom": "Jaume", "cognom": "Cardona", "Telf": "633263320"},
   "contacte2":{"nom": "Pere", "cognom":"Gomila", "Telf":"645102485"},
   "contacte2":{"nom": "David", "cognom": "Sánchez", "Telf": "676104589"}}

def ex3():
a=7.0
b=10.0
c=a**b
print(c)

a = int(input("Escriu un nombre "))
b = input("Escriu un altre nombre")
c = str(a)+b
print(c)

def menu():
    print(
          1. Salutació standard
          2. Salutació formal
          3. Salutació de poble
          4. No se loco
          5. Sortir
                 )
    op = input("Elegeix una opció: ")
    return op

def salutacio():
    print("Hola")

def salutacio_premium():
    print("Bones tardes")

def salutacio_poble():
    print("UEP! Com va?")

def nose_crazy():
    print("Calla Ja i deixem en pau, locu ")

#Programa Principal:
x = menu()
match(op):
    case 1:
        salutacio()
    case 2:
        salutacio_premium()
    case 3:
        salutacio_poble()
    case 4:
        nose_crazy()

def ex8():
    p=""
    l=[]
    while (p!="."):
        p = input("Introdueix una paraula ")
        if p!="." :
            l.append(p)
        if len(l)==4:
            print("Les paraules són: {}".format(l))
            p="."
    print("Ja hem acabat!")

def ex9():
    p=""
    l=[]
    while (p!=":"):
        p = input("Introdueix una paraula ")
        if p!=":" and p[0]=="A":
            l.append(p)
    print("Les paraules són: {}".format(l)) 
    print("Ja hem acabat!")

p=""
l=[]
while (p!="%"):
    p = input("Introdueix una paraula ")
    if p!="%":
        s= p.lower()
        s[0]=p[0].upper()+s[1:]
        l.append(p)
print("Les paraules són: {}".format(l)) 
print("Ja hem acabat!")

f = ""
l=[]
while (f!="."):
    f = input("Introdueixi una frase: ")
    if f!=".":
        s = f.lower()
        f = s.title()
        l.append(s)
print("Les paraules són: {}".format(l)) 
print("Ja hem acabat!")

def llegir_llista():
    l=[]
    p=""
    while p!=".":
        p=input("Introdueixi un element de la llista: ")
        if p!=".":
            l.append(int(p))
    return l

#Programa principal:
llista=llegir_llista()
r=[]
for i,e in enumerate(llista):
    if llista[i]==e:
        r.append(e)
print("La llista d'elements que coincideix element i posició és {}".format(r))

def sumar_llista(l):
    l=[3,4,5]
    for i in range(len(l)):
        l[i]*=3

#Programa principal:
llista=[2, 3, 4]
print(llista)
sumar_llista(llista)
print(llista)"""

def operació(a, b, c):
    c=a + b
a=3
b=4
c=0
print(c)
operació(a, b, c)
print(c)

