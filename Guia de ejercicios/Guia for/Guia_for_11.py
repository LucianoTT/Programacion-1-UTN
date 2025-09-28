# 11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
#     Informar cuántos números primos se encontraron.
#-------------------------------------------------------------------------------------------------

numero_ingresado= int(input("Digame un numero: "))
contador= 0
total= ""

for num in range(2, numero_ingresado):
    if num == 2 or num == 3 or num == 5 or num == 7:
        total= total + str(num)+(", ")
        contador += 1
    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
        total = total + str(num)+(", ")
        contador += 1

print (f"la cantidad de numeros primos es {contador}.")
print (f"Los numeros primos entre el numero 1 y {numero_ingresado} es: {total}")

