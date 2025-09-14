# 6. Crea una función que verifique si un número dado es par o impar.
#    La función debe imprimir un mensaje indicando si el número es par o impar.

def es_par_inpar():
    numero_entero= int(input("Digame un numero entero: "))
    if numero_entero % 2 == 0:
        print("Es par. ")
    else:
        print("No es par. ")