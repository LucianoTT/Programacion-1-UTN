# 1. Escribir un programa que pida un número entero positivo n y muestre en pantalla todos los
#    números pares desde 1 hasta n.


numero_positivo= int(input("Digame un numero positivo: "))

for n in range(1, numero_positivo+1):
    if n % 2 == 0:
        print(n)