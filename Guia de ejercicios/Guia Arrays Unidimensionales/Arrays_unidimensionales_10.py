# 10. Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la 
#     unión de los dos arrays.
#------------------------------------------------------------------------------------------

def union(array_1: list, array_2: list):
    union_array= ""
    for p in range(len(array_1)):
        union_array = union_array + " " + str(array_1[p])
    for n in range(len(array_2)):
        for n2 in range(len(array_1)):
            if array_1[n] != array_2[n]:
                union_array = union_array + " " + str(array_2[n])
    print (f"La union de ambos arrays es = {union_array}.")



union([1,2,3,4,5],[3,4,5,6,7])