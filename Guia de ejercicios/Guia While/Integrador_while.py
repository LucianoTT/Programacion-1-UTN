# Realizar un programa que permita que el usuario ingrese todos los números que desee.
# Una vez finalizada la carga determinar:
# A. La suma acumulada de los números negativos.
# B. La suma acumulada de los números positivos.
# C. La cantidad de números negativos ingresados.
# D. El promedio de los números positivos.
# E. El número positivo más grande.
# F. El porcentaje de números negativos ingresados, respecto del total de ingresos.

suma_positivos= 0
suma_negativos= 0
contador_negativos= 0
contador_positivos= 0
promedio_positivos= 0
mayor= 0
contador_total= 0
porcentaje= None
continuar= None

while continuar != "no":
    numero= int(input("Digame un numero: "))
    if numero >= 0:
        contador_positivos += 1
        suma_positivos += numero
        if numero >= mayor:
            mayor = numero
    elif numero <= 0:
        contador_negativos += 1
        suma_negativos += numero
    contador_total += 1
    continuar= str(input("Deseas continuar? (yes/no): "))

if continuar == "no":
    promedio_positivos= suma_positivos / contador_positivos
    porcentaje= ( contador_negativos / contador_total ) * 100
    print (f"La suma acumulada de numero negativos es: {suma_negativos}")
    print (f"La suma total de numeros positivos es: {suma_positivos}")
    print (f"La cantidad de numeros negativos ingresados es: {contador_negativos}")
    print (f"El promedio de los numeros positivos es {promedio_positivos}")
    print (f"El numero positivo mas grande es {mayor}")
    print (f"El porcentaje de numeros negativos ingresados con respecto al total es: {porcentaje} %")
