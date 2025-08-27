#1. Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima
#un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función.

def saludar(nombre):
    print ("Bievenido ", nombre)

nombre= input("¿Cual es tu nombre? ")
saludar(nombre)