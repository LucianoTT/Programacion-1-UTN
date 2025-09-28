#11. Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), 
#    muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. 
#    La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
#----------------------------------------------------------------------------------------------------------------
def principal(numero):
    if es_primo(numero) == True:
        lista_primos(numero)
    else:
        print("Numero invalido")

#----------------- es primo? ------------------------------------------
def es_primo(numero):
    if numero >= 1:
        if numero == 2 or numero == 3 or numero == 5 or numero == 7:
            return True
        elif numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0:
            return True
        else:
            return False
    else:
        return False
#------------------- listado de numeros primos--------------------------------
def lista_primos(numero_ingresado):
    contador= 0
    for num in range(1, numero_ingresado+1, 1):
        if num == 2 or num == 3 or num == 5 or num == 7:
            contador += 1
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
            contador += 1
    return contador
