# 10. Ingresar un número. Determinar si el número es primo o no.

numero= int(input("Digame un numero: "))
valor= True

for num in range(2, numero-1):
   # print(num)
    if  numero % num != 0:
        print(numero % num)
        break
if num < numero:
    print (f"{numero} No es n° primo")
else:
    print (f"{numero} Es n° primo")