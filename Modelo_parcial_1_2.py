max = 10
lista_personas= [""] * max
lista_puntuaciones= [0] * max
lista_comentarios= [""] * max


#-------------------------validaciones------------------------------------
def validar_texto(mensaje: str):
    texto= ""
    while texto == "":
        texto= str(input(mensaje))
        if texto == "":
            print("No puede dejar el espacio en blanco. ")
    return texto

def validar_numeros(mensaje: str):
    while True:
        numero= int(input(mensaje))
        if 1 <= numero <= 10:
            return numero
        else:
            print("Debe colocar un numero entre el 1 y el 10...")

#-----------------------------------ingresar datos------------------------------------------------------
def ingresar_datos(lista_personas: list, lista_puntuaciones: list, lista_comentarios: list, cantidad: int):
    while cantidad < max:
        lista_personas[cantidad]= validar_texto("Digame el nombre de la persona: ")
        lista_puntuaciones[cantidad]= validar_numeros("Digame la puntuacion: ")
        lista_comentarios[cantidad]= validar_texto("Digame el comentario: ")
        cantidad += 1
        continuar= str(input("Desea agregar otro? (y/n): ")).lower()
        if continuar != "y":
            break
    return cantidad
#----------------------------------mostrar participantes--------------------------------------------
def mostrar_participantes(lista_personas: list, lista_puntuaciones: list, lista_comentarios: list):
    
    for y in range(len(lista_personas)):
        if lista_personas[y] == "":
            break
        print(f"{y+1}. | {lista_personas[y]} | {lista_puntuaciones[y]} | {lista_comentarios[y]} .")

#----------------------------------promedio--------------------------------------------------------
def promedio(lista_personas: list, lista_puntuaciones: list, lista_comentarios: list):
    suma_total= 0
    contador= 0
    promedio= 0
    for y in range(len(lista_personas)):
        if lista_personas[y] == "":
            break
        suma_total += lista_puntuaciones[y]
        contador += 1
    if contador != 0:
        promedio = suma_total / contador
        print (f"el promedio de puntuaciones es {promedio:.2f}")
    else:
        print("Aun no ha cargado nada.")
        pass
         
#--------------------------------------bubble sort menor a mayor-----------------------------------
def bubble_sort(lista_personas: list, lista_puntuaciones: list, lista_comentarios: list):
    max= len(lista_personas)
    for n in range(max):
        for y in range(max - 1 - n):
            if lista_puntuaciones[y] > lista_puntuaciones[y + 1]:
                lista_personas[y], lista_personas[y + 1] = lista_personas[y + 1], lista_personas[y]
                lista_puntuaciones[y], lista_puntuaciones[y + 1] = lista_puntuaciones[y + 1], lista_puntuaciones[y]
                lista_comentarios[y], lista_comentarios[y + 1] = lista_comentarios[y + 1], lista_comentarios[y]
    mostrar_participantes(lista_personas, lista_puntuaciones , lista_comentarios)



#----------------------------------menu principal--------------------------------------------------
cantidad= 0
while True:

    print("-____-Menu Principal encuesta-____-")
    print("1: Ingresar participantes")
    print("2: Mostrar participantes y promedio")
    print("3: Ordenar participantes por puntuacion")
    print("4: Salir")
    opcion= str(input("Seleccione una opcion (1-4): "))

    if opcion == "1":
        ingresar_datos(lista_personas, lista_puntuaciones , lista_comentarios, cantidad)
    elif opcion == "2":
        mostrar_participantes(lista_personas, lista_puntuaciones , lista_comentarios)
        promedio(lista_personas, lista_puntuaciones , lista_comentarios)
    elif opcion == "3":
        bubble_sort(lista_personas, lista_puntuaciones , lista_comentarios)
    elif opcion == "4":
        break
    else:
        print("Opcion invalida, intentelo nuvamente.")