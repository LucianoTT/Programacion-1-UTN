# 10. Un número perfecto es aquel cuya suma de divisores propios es igual a sí mismo 
#     (ejemplo: 6= 1+2+3). Ingresar un número y determinar si es perfecto.

numero_entero= int(input("Digame un numero: "))
perfecto= 0

for num in range(1, numero_entero):
#    print(f"num = {num}")
    if numero_entero % num == 0:
        perfecto += num
#        print(f"perfecto = {perfecto}")

    
if perfecto == numero_entero:
    print(f"El numero {numero_entero} es perfecto. ")
else:
    print(f"El numero {numero_entero} no es perfecto. ")