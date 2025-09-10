# 5. Buscar un valor:
#    Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
#    Informar la posición en caso afirmativo, o indicar que no se encuentra

numeros_enteros= [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
user_num= int(input("Digame un número del 1 al 20: "))
pos= 0

for num in range(len(numeros_enteros)):
    if numeros_enteros[num] == user_num:
        pos= num
if numeros_enteros[num] == user_num:
    print (f"El numero {user_num} se encuentra en la lista, en la posicion {num}.")
else:
    print (f"El numero {user_num} no se encuenta en la lista.")