# 4. Pedir al usuario la cantidad de alumnos en una clase. Luego ingresar la nota de cada alumno
#    y contar cuántos aprobaron (nota ≥ 4) y cuántos desaprobaron.

total_alumnos= int(input("Digame la cantidad de alumnos: "))
aprobados= 0
desaprobados= 0

for cant in range(1, total_alumnos+1):
    nota= int(input("Digame la nota de los alumnos en orden: "))
    if nota >= 4:
        aprobados += 1
    elif nota < 4:
        desaprobados += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos desaprobados: {desaprobados}")