# 5: Función que retorna tupla
#    Crear una función llamada datos_usuario( ) que pida al usuario su nombre, edad y país por teclado, y
#    retorne esa información como una tupla. Mostrar la tupla resultante desde el programa principal
#---------------------------------------------------------------------------------------------------------

def datos_usuario():
    nombre= str(input("Digame el nombre: "))
    edad= str(input("Digame la edad: "))
    pais= str(input("Digame el pais: "))
    usuario = (nombre, edad, pais)
    return usuario

print (datos_usuario())
