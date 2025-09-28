# 10. Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
#----------------------------------------------------------------------------------------------------------

def primo(numero):
    if numero >= 1:
        if numero == 2 or numero == 3 or numero == 5 or numero == 7:
            return True
        elif numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0:
            return True
        else:
            return False
    else:
        return False
    
