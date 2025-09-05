# 10. Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10.
#     Calcular la suma de los números ingresados y el promedio de los mismos.

contador= 1
suma_total= 0
continuar= None

while contador <= 5 or continuar != "no":
    numero= int(input("digame un numero: "))
    suma_total += numero
    if contador < 5:
        print("Debe introducir al menos 5 numeros....")
    elif contador >= 5:
        continuar= str(input("¿Desea continuar? (yes/no): "))
        if continuar == "no":
            promedio= suma_total / contador
            print(f"La suma total es: {suma_total}")
            print(f"El promedio de los numeros es: {promedio}")
        else:
            promedio= suma_total / contador
    
    contador += 1
