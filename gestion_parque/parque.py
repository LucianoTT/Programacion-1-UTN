def mostrar_atracciones():
    print("tenemos las siguiente atracciones: Montaña Rusa, Casa del Terror y Carrusel")
    
def puede_subir(edad, atraccion):
    if edad >= 12 and atraccion == "rusa":
        return True
    elif edad > 7 and atraccion == "casaterror":
        return True
    elif edad < 6 and atraccion == "carrusel":
        return True
    else:
        return False

def calcular_precio(atraccion):
    atraccion= input("digame que atraccion quiere usar(rusa, casaterror, carrusel): ")
    costo_total= 0
    lista_atracciones= ""
    if atraccion == "rusa":
        costo_total= costo_total + 1500
        lista_atracciones += "rusa, "
        print("Atraccion agregada")
    elif atraccion == "casaterror":
        costo_total= costo_total + 1200
        lista_atracciones += "casaterror, "
        print("Atraccion agregada")
    elif atraccion == "carrusel":
        costo_total == costo_total + 800
        n_atracciones= n_atracciones + 1
        lista_atracciones += "carrusel, "
        print("Atraccion agregada")
    else:
        print("Esa atraccion no la tenemos...")
def registrar_visita():
    nombre= str(input("Nombre del visitante: "))
    edad= int(input("Edad del visitante: "))

    return resumen

def mostrar_resumen(resumen):
    print("Nombre del visitante: ", nombre)
    print("La lista de atracciones: ", lista_atracciones)
    print("Costo total: ", costo_total)