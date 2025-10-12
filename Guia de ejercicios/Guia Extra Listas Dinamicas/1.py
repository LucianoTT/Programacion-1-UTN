# 1. Cargar una lista con nombres
# Pedí al usuario que ingrese 5 nombres y guardalos en una lista. Mostrá el contenido de la lista al finalizar.
#----------------------------------------------------------------------------------------------------------------

lista= []

while True: 
    if len(lista) == 5:
        break
    lista.append(input("Digame un nombre: "))

print (lista)

