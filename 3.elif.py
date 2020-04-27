def numeros(n):
    #Genera multiples condiciones y si no se cumple una pasa a la
    #siguiente hasta encontrar la verdadera o llegar al else
    if n==1:
        print("tu numero es 1")
    elif n==2:
        print("tu numero es 2")
    elif n==3:
        print("tu numero es 3")
    elif n==4:
        print("tu numero es 4")
    else:
        print("no hay opcion")

numeros(2)
numeros(5)

def numsTupla(n):
    if n in (1,2,3,4):
        print("Tu numero es: "+n)
    else:
        print(n+" no es una opcion valida")

numeros(3)
numeros(7)

def masgrandede3(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

print("El mas grande es: "+str(masgrandede3(7,8,9)))

input()
