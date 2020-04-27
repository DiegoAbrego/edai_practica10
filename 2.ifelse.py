def obtenerMayorv2(n1,n2):
    #compara ambas variables y si la comparacion
    #resulta verdadera regresa un valor, si no regresa el otro
    if n1 < n2:
        return n2
    else:
        return n1

print("El mayor es: "+str(obtenerMayorv2(20,5)))
print("El mayor es: "+str(obtenerMayorv2(7,50)))

#el operador ternario se puede simular con if else

def mayorTernario(n1, n2):
    #si la condicion es verdadera asiga n2 de lo contrario, asigna n1
    valor = n2 if (n1 < n2) else n1
    return valor

print("El mayor es: "+str(mayorTernario(11,6)))

input()
