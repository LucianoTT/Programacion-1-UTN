#2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma,
#resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la
#función.

def operaciones(num1, num2):
    print ("Suma: ", num1 + num2)
    print ("Resta: ", num1 - num2)
    print ("Multiplicacion", num1 * num2)

num1= int(input("Escriba el primer numero: "))
num2= int(input("Escriba el segundo numero: "))
operaciones(num1, num2)
