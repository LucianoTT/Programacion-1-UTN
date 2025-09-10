# 4. Contar mayores a un valor:
#    Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado.

numeros_enteros= [101, 102, 5, 23, 582, 87, 91, 1]
contador= 0
for num in numeros_enteros:
    if num > 100:
        contador +=1

print(f"La cantidad de números mayores a 100 en las lista es: {contador}.")