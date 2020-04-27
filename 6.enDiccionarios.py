#se crea el diccionario
elementos = {'hidrogeno':1, 'helio':2, 'carbon':6}

for llave, valor in elementos.items():
    #se asigan los valores del diccionario a las variables valor y llave, se
    #imprimen y despues se itera a la siguiente posicion del diccionario
    print(llave, "=", valor)

for llave in elementos.keys():
    #solo se itera en las llaves de cada elemento del diccionario
    print(llave)

for valor in elementos.values():
    #solo se itera en los valores de cada elemento del diccionario
    print(valor)

#iterando con indices
for idx, x in enumerate(elementos):
    print("El indice es: "+str(idx)+" y el elemento: "+str(x))

def cuenta_idiom(limite):
    for i in range(limite, 0, -1):
        print(i)
    else:
        #else que corresponde al for y no a un if
        print("Cuenta finalizada")

cuenta_idiom(5)

def cuenta_idiomv2(limite):
    for i in range(limite, 0, -1):
        print(i)
        if i==3:
            break
    else:
        print("Cuenta finalizada")

cuenta_idiomv2(6)

input()
