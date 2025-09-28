nombre= str(input("Nombre del visitante: "))
edad= int(input("Edad del visitante: "))

n_atracciones= 0
costo_total= 0
lista_atracciones= ""
while n_atracciones < 3:
    #if n_atracciones <= 3:
        atraccion= input("digame que atraccion quiere usar(rusa, casaterror, carrusel): ")
        if atraccion == "rusa":
            if edad >= 12:
                costo_total= costo_total + 1500
                n_atracciones= n_atracciones + 1
                lista_atracciones += "rusa, "
                print("Atraccion agregada")
            else:
                print("No tiene la edad suficiente para esta atraccion...")
        elif atraccion == "casaterror":
            if edad >= 7:
                costo_total= costo_total + 1200
                n_atracciones= n_atracciones + 1
                lista_atracciones += "casaterror, "
                print("Atraccion agregada")
            else:
                print("No tiene la edad suficiente para esta atraccion...")
        elif atraccion == "carrusel":
            costo_total == costo_total + 800
            n_atracciones= n_atracciones + 1
            lista_atracciones += "carrusel, "
            print("Atraccion agregada")
        else:
             print("Esa atraccion no la tenemos...")
    #else:
    #print("Ya no puede subirse a mas atracciones...")

print("Nombre del visitante: ", nombre)
print("La lista de atracciones: ", lista_atracciones)
print("Costo total: ", costo_total)
    