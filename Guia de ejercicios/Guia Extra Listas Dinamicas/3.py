# 3. Eliminar un nombre usando remove( )
#    Solicitá al usuario un nombre a eliminar. Si el nombre está en la lista, removelo. Si no está, mostrá un mensaje.

lista = ["Juan", "Pedro", "Carlos"]

nombre_a_eliminar= str(input("Digame un nombre para eliminarlo de la lista: "))

for n in range(len(lista)):
    capacidad = len(lista)
    if lista[n] == nombre_a_eliminar:
        lista.remove(nombre_a_eliminar)
        print(lista)
        break
if capacidad == len(lista):
    print("Ese nombre no aparece en la lista")
    