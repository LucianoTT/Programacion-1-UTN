# 5. Solicitar al usuario un número entero y determinar si es primo (solo divisible por 1 y por sí mismo).

numero_entero= int(input("Decime un numero: "))

if numero_entero == 3 or numero_entero == 2 or numero_entero == 5 or numero_entero == 7:
    print("Es primo")
elif numero_entero % 2 != 0 and numero_entero != 2 and numero_entero % 3 != 0 and numero_entero % 5 != 0 and numero_entero % 7 != 0:
    print("Es primo")
else:
    print("No es primo....")