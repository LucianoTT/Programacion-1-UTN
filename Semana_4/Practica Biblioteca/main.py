import funciones
titulos= [""] *3
ejemplares= [0] * 3

while True:
    print ("1.Cargar titulos y ejemplares")
    print("2. mostrar catalogo completo")
    print("3. Consulta disponibilidad")
    print("4. Listar Titulos agotados")
    print("5. Agregar un nuevo Titulo")
    print("6. Actualizar ejemplares(Prestamo / Devolucion)")
    print("7. Salir")
 
    opcion= int(input("seleccione una accion: "))

    if opcion == 1:
        funciones.load_titulos(titulos, ejemplares)
        print(f" {titulos} / {ejemplares}")


    if opcion == 2:
        funciones.show_catalogo(titulos, ejemplares)
    if opcion == 3:
        pass
    if opcion == 4:
        print(ejemplares)
        funciones.agotados(titulos, ejemplares)
    if opcion == 5:
        pass
    if opcion == 6:
        pass
    if opcion == 7:
        print("Hasta luego")
        break
    else:
        print("Opcion invalida")
