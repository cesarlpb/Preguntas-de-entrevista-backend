# Dados dos arrays de enteros no vacíos, escriba una función que determine si la segundo 
# array es una subarray de la primera. 

# Un subarray de una array es un conjunto de números que no son necesariamente 
# adyacentes/contiguos en el array, pero que están en el mismo orden en que aparecen 
# en el array. 

# Por ejemplo, los números [1, 3, 4] forman una subsecuencia de la array [1, 2, 3, 4], 
# y también los números [2, 4]. [1] también es subarray de [1, 2, 3, 4].

# Notar que un solo número de un array es una subsecuencia del otro si el segundo array 
# es una subsecuencia del primera.

#%% Ejemplos

arr = [1, 2, 3, 4]
sub_arr = [1, 3, 4] 
# True

arr2 = [1, 2, 3, 4]
sub_arr2 = [2, 4] 
# True

arr3 = [1, 2, 3, 4]
sub_arr3 = [4, 1]
# False

#%% Solución 1 - bucles for

def es_subarr_valido(arr, sub_arr):
    # ¿Como podemos tener en cuenta el orden de los números que encontramos?
    contador = 0
    for el in sub_arr:  # 2, 4
        for el2 in arr: # 1, 2, 3, 4
            if el == el2:
                contador += 1
                break
    print(contador, len(sub_arr), contador == len(sub_arr))
    return contador == len(sub_arr) # si contador es 2

es_subarr_valido(arr3, sub_arr3)