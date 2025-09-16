# Cargar títulos y ejemplares
def load_titulos(titulos, ejemplares):
    print("Cargar titulo y n° de ejemplares: ")
    for titulo in range(len(titulos)):
        nombre = input("Digame el titulo:  ")
        titulos[titulo] = nombre
        ejemplares [titulo] =  int(input(f"Digame el n° de ejemplares de {nombre}: "))
        continuar = str(input("Deseas continuar? (Y/N)")).lower
        if continuar == "n":
            break
    return titulos, ejemplares

# Mostrar catálogo completo
def show_catalogo(titulos, ejemplares):
   for i in range(len(titulos)):
       print(f"{titulos[i]} -> {ejemplares[i]}")
       

# Consultar disponibilidad
def disponibilidad(titulos, ejemplares):
    for t in range(len(titulos)):
        titulo= str(input("Digame que titulo le interesa saber si esta: "))
        if titulos[t] == titulo:
            print (f"El titulo {titulo} cuenta con {ejemplares[t]}. ")


# Listar títulos agotados
def agotados(titulos, ejemplares):
    for n in range(len(ejemplares)):
        if titulos[n] != "" and ejemplares[n] == 0:
            print(f"El titulo: {titulos[n]} esta agotado. ")

# Agregar un nuevo título
def nuevo_titulo(titulos, ejemplares):
    for t in range(len(titulos)):
        if titulos[t] == "":
            titulos[t] = str(input("Digame el nombre del nuevo titulo: "))
            ejemplares[t] = int(input("Con cuantos ejemplares cuenta? "))
            continuar= str(input("Desea agregar otro? (Y/N)")).lower
            if continuar == "n":
                break
    for t in range(len(titulos)):
        if titulos [t] != "":
            continue
        print("El limite fue alcanzado")  

#Actualizar ejemplares (préstamo / devolución)
def act_ejemplares(titulos, ejemplares):
    for a in range(len(titulos)):
        editar= str(input("dime el titulo para editar la cantidad de ejemplares que quedan: "))
        if editar == titulos [a]:
            ejemplares[a] = int(input(f"Dime cuantos ejemplares tiene {editar}: "))
        continuar= str(input("¿Deseas editar otro? (Y/N) ")).lower
        if continuar == "n":
            break