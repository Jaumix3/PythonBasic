def gran():
    a = int(input("Diguis un nombre: "))
    b = int(input("Diguis un altre nombre: "))

    if a<b:
        print("{} és el nombre gran ".format(b))
    elif a>b:
        print("{} és el nombre gran".format(a))
    else:
        print("{} és igual que {}".format(a,b))
gran()
