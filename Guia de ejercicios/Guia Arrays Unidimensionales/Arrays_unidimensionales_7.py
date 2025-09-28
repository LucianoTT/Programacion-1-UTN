# 7. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las 
#    posiciones en donde se encuentra el valor máximo hallado.
#-----------------------------------------------------------------------------------------

def maximos(lista: list) -> int:
    max= 0
    for n in range(len(lista)):
        if max == lista[n]:
            pos = pos + ", " + str(n)
        elif lista[n] > max:
            max = lista[n]
            pos = str(n)
    print(pos)

maximos([2,5,1,2,4,2,3,1,2,4,5,4,4,4])