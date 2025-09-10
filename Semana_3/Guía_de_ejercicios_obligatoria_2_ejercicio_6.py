# 6. Mayor y su posición:
#    Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se encuentra.

numeros_enteros= [2,4,6,40,8,100,12]
mayor= 0
for num in range(len(numeros_enteros)):
    if numeros_enteros[num] > mayor:
        mayor= numeros_enteros[num]
        posicion= num
print (f"El número mas grande es: {mayor} y se encuenta en la posición {posicion}.")
