def convertir_a_binari(b):
    s = int(input("Idguis un nombre en binari: "))
    i = s[:-1]
    d = 0
    for e in enumerate(s):
        d=d+e**i
    return d
    
#Programa Principal: 
a = input("Introduexi un número en binari (només pot tenir 0's i 1's): ")
print("El número {}-binari és {}-decimal".format(a, convertir_a_binari(a)))
