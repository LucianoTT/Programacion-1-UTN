# A partir del ingreso de la altura en centímetros de un 
# jugador de baloncesto, el programa deberá determinar la posición del jugador
# en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

altura_jugador= int(input("¿Cual es la altura del jugador en CM? "))

if altura_jugador >= 200:
    print ("tu posicion es: Ala-Pivot o Pivot" )
elif altura_jugador <= 199 and altura_jugador >= 180:
    print ("tu posicion es: Alero" )
elif altura_jugador <= 179 and altura_jugador >= 160:
    print ("tu posicion es: Escolta" )
else:
    print ("tu posicion es: Base" )