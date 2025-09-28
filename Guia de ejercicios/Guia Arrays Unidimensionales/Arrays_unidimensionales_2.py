# 2. Escribir una función que permita ingresar la cantidad de números que reciba como 
#    parámetro.  Crear el array con la función del punto 1.
#---------------------------------------------------------------------------------------
from Arrays_unidimensionales_1 import crear_array

def ingresar_nums(numero):
    array=crear_array(numero)
    for n in range(numero):
        array[n] = int(input("Digame el numero: "))
    print (array)

ingresar_nums(5)