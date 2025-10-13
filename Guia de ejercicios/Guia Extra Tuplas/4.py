# 4: Tuplas anidadas
#    Crear una tupla llamada estudiante con el siguiente formato: estudiante = ('Lucía', 'Martínez', (8.5, 9.0,7.5))
#    Mostrar:
#    ● El nombre completo del estudiante.
#    ● El promedio de las notas almacenadas en la tupla anidada.
#---------------------------------------------------------------------------------------------------------------------

estudiante = ('Lucía', 'Martínez', (8.5, 9.0,7.5))

nombre, apellido, notas = estudiante
suma_total= 0
for n in range(len(notas)):
    suma_total += notas[n]
print (suma_total)
promedio = suma_total / len(notas)
print (f"{nombre} {apellido}")
print (f"Su promedio es {promedio:.02}")