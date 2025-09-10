# 9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número
#    ingresado. Mostrar la cantidad de divisores encontrados.

numero = int(input("Digame un numero: "))
cantidad_divisores= 1
for num in range(1, numero):
    if numero % num == 0:
        cantidad_divisores +=1

print(f"la cantidad de divisores que hay para el numero {numero} es: {cantidad_divisores}")
