# Cargar títulos y ejemplares
def load_titulos(titulos, ejemplares):
    print("Cargar titulo y n° de ejemplares: ")
    for titulo in range(len(titulos)):
        nombre = input("Digame el titulo:  ")
        if nombre == "":
            break
        titulos[titulo] = nombre
        ejemplares [titulo] =  int(input(f"Digame el n° de ejemplares de {nombre}: "))
    return titulos, ejemplares

# Mostrar catálogo completo
def show_catalogo(titulos, ejemplares):
   for i in range(len(titulos)):
       print(f"{titulos[i]} -> {ejemplares[i]}")
       

# Consultar disponibilidad
def disponibilidad(titulos, ejemplares):
    for t in range(len(titulos)):
        titulo= str(input("Digame que titulo le interesa saber"))



# Listar títulos agotados
def agotados(titulos, ejemplares):
    for n in range(len(ejemplares)):
        if titulos[n] != "" and ejemplares[n] == 0:
            print(titulos[n])

# Agregar un nuevo título
#def nuevo_titulo():

# Actualizar ejemplares (préstamo / devolución)
#def act_ejemplares():