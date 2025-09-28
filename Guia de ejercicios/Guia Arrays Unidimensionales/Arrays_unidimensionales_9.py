# 9. Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la 
#    intersección de los dos arrays.
#-----------------------------------------------------------------------------------------

def interseccion(array_1: list, array_2: list):
    interseccion_array= ""
    for p in range(len(array_1)):
        for n in range(len(array_2)):
            if array_1[p] == array_2[n]:
                interseccion_array = interseccion_array + " " +  str(array_2[n])
    print (f"La interseccion de ambos arrays es = {interseccion_array}.")



interseccion([1,2,3,4,5],[3,4,5,6,7])