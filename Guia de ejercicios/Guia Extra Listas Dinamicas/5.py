# 5. Buscar el índice de un elemento
#    Pedir un nombre al usuario, buscar si se encuentra en la lista y mostrá el índice en el que se encuentra
#    usando index( ). Si no se encuentra mostrar un cartel aclaratorio

nombre= str(input("Digame un nombre: "))
lista= ["Carlos", "Juan", "Pablo"]

if nombre in lista:
    indice= lista.index(nombre)
    print(f"El nombre {nombre} se encuentra en el indice {indice}")
else:
    print(f"El nombre {nombre} no se encuentra en la lista")