def menu():
    print("--Calculadora--\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Salir\n")

def suma():
    n1 = int(input("Ingresa el numero 1: "))
    n2 = int(input("Ingresa el numero 2: "))
    print("El resultado de la suma es: "+str(n1+n2))

def resta():
    n1 = int(input("Ingresa el numero 1: "))
    n2 = int(input("Ingresa el numero 2: "))
    print("El resultado de la resta es: "+str(n1-n2))

def multi():
    n1 = int(input("Ingresa el numero 1: "))
    n2 = int(input("Ingresa el numero 2: "))
    print("El resultado de la multiplicacion es: "+str(n1*n2))

def div():
    n1 = int(input("Ingresa el numero 1: "))
    n2 = int(input("Ingresa el numero 2: "))
    print("El resultado de la division es: "+str(n1/n2))

op=0
while op != 5:
    menu()
    op = int(input("Elige una operacion: "))
    if op == 1:
        suma()
    elif op == 2:
        resta()
    elif op == 3:
        multi()
    elif op == 4:
        div()
    elif op == 5:
        print("\nHasta Luego\n")
        input()
    else:
        print("Elige una opcion valida")
