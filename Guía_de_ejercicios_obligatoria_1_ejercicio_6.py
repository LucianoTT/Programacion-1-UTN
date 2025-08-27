#6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva
#cuántas horas y minutos sobran.

def convertir_minutos(minutos):
    horas= minutos // 60
    if minutos > 60:
        minutos_sobrantes= minutos % 60
        return horas, minutos_sobrantes
    else:
        return horas
    
minutos= int(input("Digame la cantidad de minutos: "))
print("los minutos que me dijo equivalen a estas horas y minutos: ",convertir_minutos(minutos))

    

        