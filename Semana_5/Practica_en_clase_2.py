# Ejercicio 2: Puntajes de un Torneo --------------------
# En un torneo de programación hay 4 equipos que compiten en 5 rondas.
# Cargar en una matriz 4x5 los puntajes obtenidos (enteros). Luego mostrar:
#    El puntaje total de cada equipo.
#    Qué equipo obtuvo el mayor puntaje en total.
#-----------------------------------------------------------------------------------
COLUMNAS= 5 
FILAS= 4
suma_ronda= 0
puntaje_mayor = 0

mat= [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ]
#------------------------ingresar puntajes--------------------------------
for i in range(FILAS):
    for n in range(COLUMNAS):
        valor= False
        while valor == False:
            puntaje = int(input(f"Digame el puntaje de la ronda {n+1} para el equipo {i+1}: "))
            mat[i][n] = puntaje
            valor = True
#------------------------calculo totales----------------------------
for equipo in range(FILAS):
    suma_ronda = 0
    for puntos in range(COLUMNAS):
        valor= False
        while valor == False:
            suma_ronda += mat[equipo][puntos]
            valor = True
        if suma_ronda >= puntaje_mayor:
            puntaje_mayor = suma_ronda
            primer_puesto = equipo+1
        
    print(f"¡El equipo {equipo+1} tiene un total de {suma_ronda} puntos!")
print(f"¡El equipo que obtuvo el mayor puntaje es el {primer_puesto}.")