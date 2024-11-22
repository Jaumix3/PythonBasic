def gran():
    a = int(input("Diguis un nombre: "))
    b = int(input("Diguis un altre nombre: "))

    if a<b:
        print("{} és el nombre gran ".format(b))
    else:
        print("{} és el nombre gran".format(a))

gran()
