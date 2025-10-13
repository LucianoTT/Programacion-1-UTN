# 3: Uso de in y conversión
#    Dada la tupla colores = ('rojo', 'verde', 'azul'), hacer lo siguiente:
#    ● Verificar si el color 'amarillo' está en la tupla.
#    ● Convertir la tupla en una lista, agregar el color 'amarillo', y volver a convertirla en tupla.
#    ● Mostrar la nueva tupla resultante.
#-----------------------------------------------------------------------------------------------------

colores = ('rojo', 'verde', 'azul')
 
if "amarillo" not in colores:
    colores = list(colores)
    colores.append("amarillo")
    colores = tuple(colores)
    print(colores)