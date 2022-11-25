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
# n y m -> n * m -> orden n * m
# 2 variables -> espacio no hay tanta carga

# Alternativa para llevar la cuenta del orden -> dict -> {2: 1, 4 : 3}
    # Desventaja: vamos a tener que usar otro bucle

def es_subarr_valido(arr, sub_arr):
    contador = 0
    idx = 0     # índice del último número encontrado
    for el in sub_arr:  # [2, 4] 
        for el2 in arr: # [1, 2, 3, 4] -> 1 y 3 -> 3 > 1
                        # [4, 1] -> 0 > 3 -> False
            if el == el2 and arr.index(el2) >= idx:
                idx = arr.index(el2)
                print(el, el2, idx)
                contador += 1
                break

    print(contador, len(sub_arr), contador == len(sub_arr))
    return contador == len(sub_arr) # si contador es 2
#%% Tests iniciales
es_subarr_valido(arr, sub_arr)   # True
es_subarr_valido(arr2, sub_arr2) # True
es_subarr_valido(arr3, sub_arr3) # Debe retornar False
#%% Solución 2 con while


#%% Solución - Marta
''' Por cada elemento (value) en el sub_array
   miramos si encontramos ese elemento en el array.
   En caso de encontrarlo salimos de ese bucle while con la posición i
   y buscamos el nuevo elemento(value) a partir de la posición i del anterior.
   En caso de no encontrarlo el índice será igual a len(arr)
'''
def subArr(arr, sub_arr):
   # si el subArray es menor no buscamos, retornamos false.
   if len(arr) < len(sub_arr): return False
   else:
       i = 0
       for value in sub_arr:
           b = False
           while i < len(arr) and not b:
               b = (value == arr[i]) # si es igual es true, sino es false
               i+= 1
       return b


