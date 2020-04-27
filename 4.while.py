def cuenta(limite):
    i = limite
    while True:
    #ciclo infinito while
        print(i)
        i=i-1
        if i==0:
            break
        #sin embargo el ciclo de control se rompera cuando i=0
        #ya que el if se volvera verdadero y se ejecuara el break
cuenta(10)

def factorial(n):
    i=2
    tmp=1
    while i <n+1:
        #la condicion se ejecuara mientras i sea menor al numero que entro +1
        #con cada ciclo de ejecucion, i aumenta en 1
        tmp=tmp*i
        i=i+1
    return tmp

print(factorial(4))

print(factorial(6))

input()
