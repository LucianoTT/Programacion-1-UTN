# 10. Función para buscar la primera aparición de un valor:
#     Escribir una función que reciba un array de enteros y un número a buscar.
#     La función debe retornar la posición de la primera aparición de ese número o -1 si no se encuentra.

def primer_aparicion(numeros_enteros, a_buscar):
    pos= None
    for num in range(len(numeros_enteros)):
        if numeros_enteros[num] == a_buscar:
            pos = num
            return pos

    if pos == None:
        return -1


primer_aparicion([2,7,8,23,6,10,6,87,7], 6)