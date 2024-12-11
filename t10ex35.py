def any_depas(any1):
    if (any1 % 4 == 0 and any1 % 100 != 0) or (any1 % 400 == 0):
        return True
    else:
        return False
año = int(input("Diguis un any (aaa): "))

if any_depas(año):
    print("El año {} es un año de traspas.".format(año))
else:
    print("El año {} no es un año de traspas.".format(año))
