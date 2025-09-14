# 7. Generar un número secreto entre 1 y 50 (puede fijarse manualmente). El usuario debe
#    adivinarlo. El programa le debe indicar si el número ingresado es mayor o menor al secreto, y
#    terminar cuando lo adivine.

numero_secreto= 22

while True:
    propuesta= int(input("Adivina el número entre el 1 y el 50: "))
    if propuesta <= 0 or propuesta >= 51:
        print("Numero invalido")
    elif numero_secreto > propuesta:
        print("Tu número es muy bajo")
    elif numero_secreto < propuesta:
        print("Tu número es muy alto")
    elif numero_secreto == propuesta:
        print("¡Lo has adivinado!")
        break
    