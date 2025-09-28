#Ejercicio 1: Registro de Temperaturas
#Una estación meteorológica registra las temperaturas diarias de una semana (7 días) en 3 horarios (mañana, tarde y noche).
#Cargar en una matriz 7x3 las temperaturas (números enteros) y mostrar:
#    El promedio de temperatura de cada día.
#    El promedio general de toda la semana.
#----------------------------------------------------------------------------------------
COLUMNAS= 3
FILAS= 7
DIAS= ["Lunes","Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
RANGO= ["Mañana", "Tarde", "Noche"]
promedio_dia= 0
promedio_semana= 0
suma_de_la_semana= 0

mat= [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0],
]
#-------------ingreso datos-----------------------
for d in range(FILAS):
    print(f"Dia: {DIAS[d]}")
    for t in range(COLUMNAS):
        valor_valido = False
        while valor_valido == False:
            temperatura= int(input(f"Ingresa la temperatura de la {RANGO[t]}: "))
            mat[d][t] = temperatura
            valor_valido = True

#-------------calculo promedio del dia y semana-------------------------
for k in range(FILAS):
    suma_del_dia = 0
    for dia in range(COLUMNAS):
        suma_del_dia += mat[k][dia]
    suma_de_la_semana += suma_del_dia
    promedio_dia= suma_del_dia / COLUMNAS
    print(f"El dia {DIAS[k]} tuvo un promedio de {promedio_dia:.2f} ")

    
promedio_semana= suma_de_la_semana / (FILAS * COLUMNAS)
print(f"El promedio de la semana es {promedio_semana:.2f}")
