# 6. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición 
#    del valor máximo encontrado.
#------------------------------------------------------------------------------------------------

def maximo(lista: list) -> int:
    max= 0
    for n in range(len(lista)):
        if lista[n] > max:
            max = lista[n]
            pos = n
    return pos

maximo([2,4,123,4,289,1000,25,7,86,423])