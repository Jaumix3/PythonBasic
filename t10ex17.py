def tf():
    a = input("Diguis una lletra: ")

    if a in ("a","e","i","o","u"):
        print("{} és una vocal ".format(a))
    else:
        print("{} és una consonant ".format(a))

tf()