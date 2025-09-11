# 9. Intercambiar elementos pares por ceros:
#    Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array resultante.

numeros_enteros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in range(len(numeros_enteros)):
    if numeros_enteros[num] % 2 == 0:
        numeros_enteros[num]= 0

print(numeros_enteros)