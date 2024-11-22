"""""
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


a=7.0
b=10.0
c=a**b
print(c)"""

a = int(input("Escriu un nombre "))
b = input("Escriu un altre nombre")
c = str(a)+b
print(c)