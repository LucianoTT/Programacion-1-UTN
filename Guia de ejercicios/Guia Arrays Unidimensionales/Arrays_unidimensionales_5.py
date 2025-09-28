# 5. Escribir una función que calcule y retorne el producto de todos los elementos de la lista que 
#    recibe como parámetro.
#---------------------------------------------------------------------------------------------------

def producto(lista: list) -> int:
    producto_total= 1
    for n in range(len(lista)):
        producto_total *= lista[n]
    print(producto_total)
    return producto_total

producto([2, 2, 2, 2])