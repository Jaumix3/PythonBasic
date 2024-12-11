x = int(input("Escriu un nombre menor que 100: "))
y=0.0
for i in range(x,1,-4):
    y += i**2

print("La suma dels quadrats de 4 en quatre de {} és {} ".format(x, y))