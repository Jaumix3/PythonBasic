def llegir_llista():
   l=[]  
   a="a"
   while a!=".":
       a=input("Introdueix un nom: ")
       if a!=".":
           l.append(a)
   return l




def retorna_nova_llista(l):
   return l[1:-1]


#Programa principal
l=llegir_llista()
s=retorna_nova_llista(l)
print("{} es transforma en {}".format(l,s))
