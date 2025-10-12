# 2. Insertar un nuevo nombre en una posición específica
#    Usá el método insert( ) para agregar un nombre nuevo en la segunda posición (índice 1) de la lista anterior.
#-----------------------------------------------------------------------------------------------------------------

lista= []

while True: 
    if len(lista) == 5:
        break
    lista.append(input("Digame un nombre: "))

print (lista)
lista.insert(1, "miguelangelo")
print ("_Nueva lista_")
print (lista)