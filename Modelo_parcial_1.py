max= 10
lista_persona = [""] * 10
lista_puntuaciones = [0] * 10
lista_comentarios = [""] * 10



def ingresar_participantes(lista_persona, lista_puntuaciones, lista_comentarios):
    for n in range(len(lista_persona)):
        #Nombre del cliente
        while lista_persona[n] == "":
            lista_persona[n]= str(input("Nombre del cliente: "))
            if lista_persona[n] == "":
                print("no puede ingresar un valor en blanco. ")
        #Puntuacion del cliente
        while lista_puntuaciones[n] < 1 or lista_puntuaciones[n] >= 11:
            lista_puntuaciones[n]= int(input("Puntuacion de satisfaccion (1 a 10): "))
            if lista_puntuaciones[n] < 1 or lista_puntuaciones[n] >= 11:
                print("debe ingresar un valor entre el 1 y el 10. ")
        #Comentario del cliente
        while lista_comentarios[n] == "":
            lista_comentarios[n]= str(input("Comentario: "))
            if lista_comentarios == "":
                print("no puede ingresar un valor en blanco. ")
        continuar = str(input("Desea continuar? (y/n): "))
        if n == len(lista_persona)-1:
            print("Ya no puedes ingresar mas participantes...")
            break
        if continuar == "n":
            break
    
    return(lista_persona, lista_puntuaciones, lista_comentarios)


def puntuaciones_comentarios(lista_persona, lista_puntuaciones, lista_comentarios):
    suma_notas= 0
    contador= 0
    for n in range(len(lista_persona)):
        if lista_persona[n] == "":
#           print("Fin de la lista")
            break
        print (f"Nombre: {lista_persona[n]}, Puntuacion:  {lista_puntuaciones[n]}, Comentario: {lista_comentarios[n]} ")
    for n in range(len(lista_puntuaciones)):
        if lista_puntuaciones[n] == 0:
#            print("Fin de las puntuaciones")
            break
        suma_notas += lista_puntuaciones[n]
        contador += 1
    promedio= suma_notas / contador
    print (f"El promedio de las notas es: {promedio}. ")

def ordenar(lista_persona, lista_puntuaciones, lista_comentarios):
    size= max    
    for n in range(size):
        for i in range(size - 1 - n):
            if lista_puntuaciones[i] < lista_puntuaciones[i + 1]:
                lista_persona[i], lista_persona[i + 1] = lista_persona[i + 1], lista_persona[i]
                lista_puntuaciones[i], lista_puntuaciones[i + 1] = lista_puntuaciones[i + 1], lista_puntuaciones[i]
                lista_comentarios[i], lista_comentarios[i + 1] = lista_comentarios[i + 1], lista_comentarios[i]
    for y in range(len(lista_persona)):
        if lista_persona[y] == "":
            break
        print (f"Nombre: {lista_persona[y]}, Puntuacion:  {lista_puntuaciones[y]}, Comentario: {lista_comentarios[y]} ")
        
while True:
    print("--- Menú Encuesta de Satisfacción ---")
    print("1. Ingresar participantes")
    print("2. Mostrar participantes y promedio")
    print("3. Ordenar participantes por puntuación")
    print("4. Salir")
    seleccion = input("Seleccione una opción (1-4): ")
    if seleccion == "1":
        ingresar_participantes(lista_persona, lista_puntuaciones, lista_comentarios)
    elif seleccion == "2":
        puntuaciones_comentarios(lista_persona, lista_puntuaciones, lista_comentarios)
    elif seleccion == "3":
        ordenar(lista_persona, lista_puntuaciones, lista_comentarios)
    elif seleccion == "4":
        break
    else:
        print("Opción inválida. Intente nuevamente.")