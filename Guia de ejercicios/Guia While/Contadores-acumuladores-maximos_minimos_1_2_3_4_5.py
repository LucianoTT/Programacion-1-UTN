# 1. Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

contador1= 1
while contador1 is not 11:
    print(contador1)
    contador1 += 1

print ("------------------------")
# 2. Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

contador2= 10
while contador2 is not 0:
    print(contador2)
    contador2 -= 1

print ("------------------------")
# 3. Mostrar la suma de los números desde el 1 hasta el 10.

contador3= 1
sumatotal= 0
while contador3 is not 11:
    sumatotal += contador3
    contador3 +=1
    print (f"{sumatotal} + {contador3}")

print ("------------------------")
# 4. Mostrar la suma de los números pares desde el 1 hasta el 10.

contador4= 1
sumatotal2= 0

while contador4 is not 10:
    contador4 += 1
    if contador4 % 2 == 0:
        sumatotal2 += contador4
        print (f"{sumatotal2}")

print ("------------------------")
# 5. Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio.
#    Mostrar la suma y el promedio por pantalla.

contador5= 1
sumatotal3= 0
promedio= 0

while contador5 is not 6:
    numeros= input("Introduzca un numero: ")
    sumatotal3 += contador5
    contador5 += 1
    if contador5 == 6:
        promedio= sumatotal3 / 5
        print (f"la suma total es: {sumatotal3} y su promedio es {promedio}.")


