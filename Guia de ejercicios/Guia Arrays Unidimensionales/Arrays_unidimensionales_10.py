# 10. Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la 
#     unión de los dos arrays.
#------------------------------------------------------------------------------------------

def union(array_1: list, array_2: list):
    union_arrays= array_1
    for n in  array_2:
        if n not in union_arrays:
            union_arrays += [n]


    print (f"La union de ambos arrays es = {union_arrays}.")



union([1,2,3,4,5],[3,4,5,6,7])