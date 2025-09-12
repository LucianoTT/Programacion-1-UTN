# 6. El usuario debe ingresar una cantidad indefinida de números (termina con cero). Calcular el
#    promedio de los números positivos y el promedio de los negativos por separado.

total_numeros= 0
total_positivos= 0
total_negativos= 0
contador_positivos= 0
contador_negativos= 0

while True:
    numero= int(input("Digame un numero: "))
    total_numeros += 1
    if numero > 0:
        total_positivos += numero
        contador_positivos += 1
    elif numero  < 0:
        total_negativos += numero
        contador_negativos += 1
    elif numero == 0:
        promedio_positivos= total_positivos / contador_positivos
        promedio_negativos= total_negativos / contador_negativos
        print(f"El promedio de numeros positivos es: {promedio_positivos}")
        print(f"El promedio de numeros negativos es: {promedio_negativos}")
        break


