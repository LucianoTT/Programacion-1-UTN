# 8. Ingresar 10 números enteros. Determinar el máximo y el mínimo.

contador= 0
mayor= 0
menor= None

while contador is not 11:
    numero= int(input("Digame un numero entero: "))
    if numero > mayor:
        mayor = numero
    if menor == None:
        menor = numero
    elif numero < menor:
        menor = numero
    contador += 1
    if contador == 10:
        print(f"El numero mayor es: {mayor} y el menor es: {menor}.")