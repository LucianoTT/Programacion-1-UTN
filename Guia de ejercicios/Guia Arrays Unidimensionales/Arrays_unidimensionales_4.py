# 4. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el 
#    promedio de los números positivos.
#-----------------------------------------------------------------------------

def promedio(lista: list) -> int:
    suma_total= 0
    promedio= 0
    contador= 0
    for n in range(len(lista)):
        if lista[n] > 0:
            suma_total += lista[n]
            contador += 1
    promedio= suma_total / contador
    return promedio

promedio([10,10,1,-10,-3,-4,0])