# 2. Pedir al usuario un número entero e imprimir la tabla de multiplicar de ese número desde el 1
#    hasta el 10.

numero_entero= int(input("Digame un numero entero: "))
resultado= 0

for num in range(1, 11):
    resultado = numero_entero * num
    print (f"{numero_entero} X {num} = {resultado}")