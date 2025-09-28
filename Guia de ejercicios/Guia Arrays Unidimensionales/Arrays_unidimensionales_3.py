# 3. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el 
#    promedio de todos los números. 
#-------------------------------------------------------------------------------------------

def promedio(lista: list) -> int:
    suma_total= 0
    promedio= 0
    contador= 0
    for n in range(len(lista)):
        suma_total += lista[n]
        contador += 1
    promedio= suma_total / contador
    return promedio

promedio([10,10,1])

