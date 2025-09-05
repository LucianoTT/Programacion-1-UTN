# 9. Solicitar al usuario que ingrese como mínimo 5 números.
#    Calcular la suma de los números ingresados y el promedio de los mismos.

contador= 1
suma_total= 0
promedio= 0

while contador != 6:
    numero= int(input("digame un numero: "))
    suma_total += numero

    if contador == 5:
        promedio= suma_total / 5
        print(f"La suma total es: {suma_total}")
        print(f"El promedio de los numeros es: {promedio}")
    contador += 1