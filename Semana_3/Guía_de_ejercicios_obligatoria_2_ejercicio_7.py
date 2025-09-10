# 7. Invertir orden:
#    Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.

numeros_enteros= [1,2,3,4,5,6]

for num in range(len(numeros_enteros)-1, -1, -1):
    print (numeros_enteros[num])