#7. Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si
#es mayor de edad (18 años o más) devolviendo un booleano. Luego, el programa debe pedir la
#edad al usuario y mostrar un mensaje apropiado.

def verificar_acceso(edad):
    if edad >= 18:
        return True
    else:
        return False
    
edad=int(input("Dime tu edad y te dire si puede entrar: "))
print(verificar_acceso(edad))