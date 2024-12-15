def llegir_llista():
   l=[]
   a="a"
   while a!=".":
       a=input("Introdueix un número: ")
       if a!=".":
           l.append(int(a))
   return l


def elimina_duplicats(l):
   s = set(l)
   return list(s)


#programa principal
l=llegir_llista()
r=elimina_duplicats(l)
print("La llista {} queda així {}".format(l,r)
