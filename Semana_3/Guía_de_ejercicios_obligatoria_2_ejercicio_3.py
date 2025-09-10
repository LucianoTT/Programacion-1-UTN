# 3. Promedio de valores:
#    Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular 
#    y mostrar el promedio de los valores.

numeros_reales= [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
suma_total= 0.0
for num in numeros_reales:
    suma_total += num
    promedio= suma_total / len(numeros_reales)

print(f"La suma de los números reales {suma_total} y su promedio es {promedio}.")
