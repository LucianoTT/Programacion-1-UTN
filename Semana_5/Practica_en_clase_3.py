# Ejercicio 3: Control de Producción ---------------------------------
#  Una fábrica produce 3 productos y mide la producción durante 4 días.
#  Cargar en una matriz 3x4 las cantidades producidas. Mostrar:
#    La producción total de cada producto.
#    La producción total de cada día.
#    Cuál fue el día con mayor producción total.

COLUMNAS= 4
FILAS= 3
total_dia= 0

mat= [[0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
    ]

for n in range(FILAS):
    prod_total= 0
    for y in range(COLUMNAS):
        valor= False
        while valor == False:
            producido = int(input(f"Digame la cantidad producida el dia {y+1}: "))
            mat[n][y]= producido
            prod_total += producido
            valor = True
    #total_dia += mat[n][n]
    print (f"El producto {n+1} ha producido {prod_total} en total.")
for d in range(FILAS):
    total_dia += mat[n][n]
print(f"el total producido del dia {FILAS} es: {total_dia}. ")

    
