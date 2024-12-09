def num_mayus(s):
        num=0
        for e in s:
            if e.isupper():
                num += 1
        return num

a = input("Intridueix una paraula amb MAJÚSCULES i minúscules: ")
print("El número de majúscules que té la paraula {} és de {}".format(a,num_mayus(a)))