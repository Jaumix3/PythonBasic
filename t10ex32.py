def variant1():
        def llegir_llista():
            l=[]
            a="a"
            while a!=".":
                a=input("Introdueix un nom: ")
                if a!=".":
                    l.append(a)
            return l

        def noms_comencen_per(l,c):
            m=[]
            for e in l:
                if e[-1]==c.upper() or e[-1]==c.lower():
                    m.append(e)
            print("Els elements de la llista {} que comencen per {} són {}".format(l,c,m))

        #Programa Princiapal
        l = llegir_llista()
        c = input("Introdeix un caràcter: ")
        noms_comencen_per()

def variant2():
    def llegir_llista():
        l=[]
        a="a"
        while a!=".":
            a=input("Introdueix un nom: ")
            if a!=".":
                l.append(a)
        return l

    def noms_comencen_per(l,c):
        m=[]
        for e in l:
            senar = len(e)%2==1
            if senar:
                aux=len(e)//2+1
                if e[aux]==c.upper() or e[aux]==c.lower():
                    m.append(e)
            else:
                aux= len(e)//2-1
                if e[aux]==c.upper() or e[aux]==c.lower() or e[aux+1]==c.upper() or e[aux]==c.lower():
                    m.append(e)
        print("Els elements de la llista {} que comencen per {} són {}".format(l,c,m))

    #Programa Princiapal
    l = llegir_llista()
    c = input("Introdeix un caràcter: ")
    noms_comencen_per()

variant2()