# 5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
#    Mostrar la suma y el promedio de todos los números.

suma_total= 0

for num in range(1, 11):
    numero= int(input("Digame un numero: "))
    if numero == 0:
        break
    suma_total += numero
    promedio = suma_total / num
print(f"la suma total es: {suma_total} y su promedio es: {promedio}.")