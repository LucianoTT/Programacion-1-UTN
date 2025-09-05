# 6. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
#    Calcular la suma de los números ingresados y el promedio de los mismos.

continuar= None
sumatotal= 0
contador= 0

while continuar != "no":    
    numero= int(input("Digame un numero: "))
    sumatotal += numero
    if contador >= 1:
        print (f"El total de la suma de los numeros que me dijo es: {sumatotal}")
    contador += 1
    continuar= str(input("¿Desea continuar? (yes/no): "))
