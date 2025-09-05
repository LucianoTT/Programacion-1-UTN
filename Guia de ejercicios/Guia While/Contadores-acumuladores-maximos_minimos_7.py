# 7. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
#    Calcular la suma de los números positivos y el producto de los negativos.

continuar2= None
suma_positivos= 0
producto_negativos= None


while continuar2 != "no":
    numero= int(input("Digame un numero que no sea 0: "))
    if numero > 0:
        if suma_positivos == 0:
            suma_positivos= numero
            print (f"El unico numero positivo que me dijo es: {suma_positivos}")
        else: 
            suma_positivos += numero
            print (f"El total de la suma de los numeros que me dijo es: {suma_positivos}")
    if numero < 0:
        if producto_negativos == None:
            producto_negativos= numero
            print (f"El unico numero negativo que me dijo es: {producto_negativos}")
        else:
            producto_negativos *= numero
            print (f"El producto de los numeros negativos que me dijo es: {producto_negativos}")
    else:
        print("El numero que me dijo no es valido")
    continuar2= str(input("¿Desea continuar? (yes/no): "))