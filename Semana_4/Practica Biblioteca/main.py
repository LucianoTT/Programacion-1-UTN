import funciones
titulos= [""] *20
ejemplares= [0] * 20

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

    if opcion == 2:
        funciones.show_catalogo(titulos, ejemplares)

    if opcion == 3:
        funciones.disponibilidad(titulos, ejemplares)

    if opcion == 4:
        funciones.agotados(titulos, ejemplares)

    if opcion == 5:
        funciones.nuevo_titulo(titulos,ejemplares)

    if opcion == 6:
        funciones.act_ejemplares(titulos,ejemplares)

    if opcion == 7:
        print("Hasta luego")
        break
