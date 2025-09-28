# Ejercicio 3: Control de Producción ---------------------------------
#  Una fábrica produce 3 productos y mide la producción durante 4 días.
#  Cargar en una matriz 3x4 las cantidades producidas. Mostrar:
#    La producción total de cada producto.
#    La producción total de cada día.
#    Cuál fue el día con mayor producción total.
#---------------------------------------------------------------------
COLUMNAS= 4
FILAS= 3
matriz= [[0] * COLUMNAS for _ in range(FILAS)]
mayor_produccion= 0
#----------------------Introducir datos-------------------------------

for p in range(FILAS):
    for d in range(COLUMNAS):
        matriz[p][d] = int(input(f"Digame lo producido del dia {d+1} para el producto {p+1} :"))
#-------------------------suma total productos--------------------------
for t in range(FILAS):
    suma_total_productos= 0
    for x in range(COLUMNAS):
        suma_total_productos += matriz[t][x]
    print(f"Se produjo un total de: {suma_total_productos}, del producto {t+1}. ")
#--------------------------suma total productos del dia-------------------
for y in range(COLUMNAS):
    suma_del_dia= 0
    for n in range(FILAS):
        suma_del_dia += matriz[n][y]
    if mayor_produccion < suma_del_dia:
        mayor_produccion = suma_del_dia
        dia= y
    print(f"En el dia {y+1} se produjo un total de {suma_del_dia} de los tres productos.")
print(f"El dia que mas se produjo fue el dia {dia+1}, con un total de {mayor_produccion} productos")





    
