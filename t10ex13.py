def menu():
  op=0
  while op<1 or op>5:
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4 Dividir")
    print("5.Cambiar base ")
    print("--------------------")
    op = int(input("Introdueix una opció: "))
    return op     
def sumar():
  a = int(input("Introduieixi el primer element" ))
  b = int(input("Introduieixi el segon element" ))
  c = a + b
  print("El resultat de sumar {} més {} és {}".format(a, b, c))

def restar():
  a = int(input("Introduieixi el primer element" ))
  b = int(input("Introduieixi el segon element" ))
  c = a - b
  print("El resultat de restar {} i {} és {} ".format(a, b, c))

def multiplicar():
  a = int(input("Introduieixi el primer element" ))
  b = int(input("Introduieixi el segon element" ))
  c = a * b
  print("El resultat de multiplicar {} per {} és {}".format(a, b, c))

def dividir():
  a = int(input("Introduieixi el primer element" ))
  b = int(input("Introduieixi el segon element" ))
  c = a / b
  print("El resultat de dividir {} entre {} és {}".format(a, b, c))
def canvBase():
   a = int(input("Introdueix el nombre que vulguis convertir en decimal: "))
   print(f"En binari és {bin(a)}")
   print(f"En octal és {oct(a)}")
   print(f"En hexadecimal és {hex(a)}")
   print(f"En decimal és {a}")


a = True
while a:
    op = menu()
    match op:
        case 1:
          sumar()
        case 2:
           restar()
        case 3:
            multiplicar()
        case 4:
            dividir()
        case 5:
          a = canvBase()
        case 6:
          a = False
          print ("Gràcies i Adéu!")  
        case _:
          print("Opció no valida \n")  
