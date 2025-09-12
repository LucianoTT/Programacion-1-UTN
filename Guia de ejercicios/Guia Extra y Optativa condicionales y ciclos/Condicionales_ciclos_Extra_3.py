# 3. Leer un número entero positivo y calcular la suma de sus dígitos usando un ciclo.

numero_positivo= str(input("Digame un numero positivo de 2 digitos o mas: "))
total= 0

for num in numero_positivo:
    total= total + int(num)

print(total) 