# 8. Ingresar un número entero positivo y calcular su factorial (ejemplo: 5! = 5×4×3×2×1).

numero_entero= int(input("Digame un numero entero positivo: "))
factorial= 1

for num in range(1, numero_entero+1):
    factorial= factorial * num

print(factorial)