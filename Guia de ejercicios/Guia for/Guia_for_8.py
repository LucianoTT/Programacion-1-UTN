# 8. Realizar un programa que permita mostrar una pirámide de números
#    Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
#    1
#    12
#    123
#    1234
#    12345

n= int(input("Digame un numero: "))

for num in range(1, n + 1):
    piramide = ""
    for num2 in range(1, num + 1):
        piramide += str(num2)
    print(piramide)
