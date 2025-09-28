# 8. Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
#       a. Una lista de nombres (lista_nombres).
#       b. Un nombre a buscar en la lista (nombre_antiguo).
#       c. Un nombre de reemplazo (nombre_nuevo).
#    La función debe realizar las siguientes acciones:
#       Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
#       Retornar la cantidad total de reemplazos realizados.
#----------------------------------------------------------------------------------------------------

def reemplazar_nombres(lista_nombres: list, nombre_antiguo: str, nombre_nuevo: str) -> int:
#    print(f"lista antes del cambio {lista_nombres}")
    contador= 0
    for n in range(len(lista_nombres)):
        if lista_nombres[n] == nombre_antiguo:
            lista_nombres[n] = nombre_nuevo
            contador += 1
#    print(f"Lista despues del cambio {lista_nombres}")
#    print(f"Cantidad de cambios: {contador}")
    return contador

reemplazar_nombres(["carlos", "pedro", "juana", "pedro"], "pedro", "hermenegildo")