#4. Crear una función buscar_mayor que reciba tres números y devuelva los tres números
#ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números ordenados.

def buscar_mayor(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        if num2 >= num3:
            return num1, num2, num3
        else:
            return num1, num3, num2
    elif num2 >= num1 and num2 >= num3:
        if num1 >= num3:
            return num2, num1, num3
        else:
            return num2, num3, num1

    elif num3 >= num1 and num3 >= num2:
        if num1 >= num2:
            return num3, num1, num2
        else:
            return num3, num2, num1
        
num1= int(input("Escriba el primer numero: "))
num2= int(input("Escriba el segundo numero: "))
num3= int(input("Escriba el tercera numero: "))
print(buscar_mayor(num1, num2, num3))