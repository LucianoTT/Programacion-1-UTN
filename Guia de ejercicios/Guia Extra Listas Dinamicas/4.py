# 4. Usar el operador in
#    Mostrá un mensaje indicando si el nombre "Juan" está o no en la lista.

lista= ["Juans", "Pedro", "Carlos","Juan"]
nombre = "Juan"

if nombre in lista:
    print(f"El nombre {nombre} esta en la lista")
else:
    print(f"El nombre {nombre} no esta en la lista")