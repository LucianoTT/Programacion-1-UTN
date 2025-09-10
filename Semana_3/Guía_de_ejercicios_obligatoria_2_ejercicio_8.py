# 8. Comparar dos arrays:
#    Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
#    y mostrar un mensaje indicando si son o no iguales.

cajon_1= [58, 19, 198, 237, 8728]
cajon_2= [58, 19, 198, 237, 8728]
contador= 0

for valor in range(len(cajon_1)):
    for valor2 in range(len(cajon_2)):
        if cajon_1[valor] == cajon_2[valor2]:
            contador += 1
            pass
        if contador == 5:
            print(f"Son iguales")
            break
    if valor == 4 and contador < 5:
        print(f"No son iguales")
