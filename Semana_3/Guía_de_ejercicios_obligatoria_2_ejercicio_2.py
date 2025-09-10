# 2. Sumar todos los elementos:
#    Declarar un array de 10 enteros. Cargarlo por teclado.
#    Calcular y mostrar la suma de todos los elementos.

numeros_enteros= [1,2,3,4,5,6,7,8,9,10]
suma_total= 0
for num in numeros_enteros:
    suma_total += num

print(f"La suma de los números enteros es {suma_total}.")