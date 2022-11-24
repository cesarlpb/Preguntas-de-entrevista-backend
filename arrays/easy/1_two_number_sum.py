# Escriba una función que tome un array no vacío de enteros distintos y un entero que representa una suma objetivo. 
# Si dos números cualesquiera del array de entrada suman suma hasta la suma objetivo, la función debe devolverlos en un array, 
# en cualquier orden. Si no hay dos números que sumen la suma objetivo, la función debe devolver  un array vacío.

# Ejemplos
#%% 1
array_de_ejemplo1 = [3, 5, -4, 8, 11, 1, -1, 6]
suma_objetivo1 = 10
output1 = [11, -1]
#%% 2
array_de_ejemplo2 = [3, 5, -4, 8, 11, 1, -1, 6]
suma_objetivo2 = 20
output2= []

#%% Tests
arr_test_1 = [3, 5, -4, 8, 11, 1, -1, 6]
arr_test_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
arr_test_3 = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
test_dict = {
    "1": (arr_test_1, 10),
    "2": (arr_test_1, 20),
    "3": ([4, 6], 10),
    "4": ([4, 6, 1], 5), 
    "5": ([4, 6, 1, -3], 3), 
    "6": ([1, 2, 3, 4, 5, 6, 7, 8, 9], 17), 
    "7": (arr_test_2, 18),
    "8": ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18),
    "9": ([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5),
    "10":(arr_test_3, 163),
    "11":(arr_test_3, 164), 
    "12":([3, 5, -4, 8, 11, 1, -1, 6], 15),
    "13":([14], 15),
    "14":([15], 15)
}
print(test_dict)

#%% Solución - 1 -> dos bucles for
# Dos bucles for -> n^2 en tiempo siendo n = len(lista)
# space -> no requiere guardar muchos datos
def sumarDosNumeros(lista, target):
    for i in range(len(lista)-1):
        a = lista[i]
        for j in range(i+1, len(lista)):
            b = lista[j]
            if a + b == target:
                return [a, b]
    return []
# Probamos los ejemplos:
res1 = sumarDosNumeros(array_de_ejemplo1, suma_objetivo1)
res2 = sumarDosNumeros(array_de_ejemplo2, suma_objetivo2)

if res1 == output1:
    print("Test 1 -", res1, output1, True)
if res2 == output2:
    print("Test 2 -", res2, output2, True)
#%% Solución - 2
# n -> time, n -> space
def sumarDosNumeros2(lista, target):
    dic = {} # hashmap, tabla, tabla hash... -> dict -> key, value
    for a in lista:
        # a + b = target -> b = target - a 
        b = target - a
        if b in dic:
            return [a, b]
        else: 
            dic[a] = True
        # print(dic)
    return []
sumarDosNumeros2(array_de_ejemplo1, suma_objetivo1) # [-1, 11]
sumarDosNumeros2(array_de_ejemplo2, suma_objetivo2) # []
#%% Solución - 3 
# n en tiempo
# poco en espacio -> solo se usan las dos variables de índices
def sumarDosNumeros3(lista, target):
    lista.sort() # ordenamos lista asc
    izq = 0
    der = len(lista) - 1
    while izq < der:
        suma = lista[izq] + lista[der]
        if suma == target:
            return [lista[izq], lista[der]]
        elif suma < target:
            izq += 1
        elif suma > target:
            der -= 1
    return []

sumarDosNumeros3(array_de_ejemplo1, suma_objetivo1) # [-1, 11]
sumarDosNumeros3(array_de_ejemplo2, suma_objetivo2) # []

#%% Solución - Marta
# arr -> lista 
# target -> N
def sumaDos(arr, N):
   b = True
   i,j = 0, 0
   sol = []
   while b and j != len(arr):
       while b and i < len(arr):
           if arr[j] + arr[i] == N:
               b = False
               sol = [arr[j], arr[i]]
           i += 1
       j += 1
       i = j+1
   return sol

array_de_ejemplo = [3, 5, -4, 8, 11, 1, -1, 6]
suma_objetivo = 10
sumaDos(array_de_ejemplo, suma_objetivo)

#%% Solución - Marta
# lista -> nums
# n en tiempo
# espacio -> n
def twoSum(nums, target):
    dif={}
    # i es el índice: 0, 1, ... len(nums) - 1
    # num es el valor: 3, 5, -4 ... 6
    for i, num in enumerate(nums):
        n=target-num
        if n not in dif:
            dif[num]=i
            # print(dif)
        else:
            # return [dif[n], i]  # devuelve índices de 11 y -1 -> [4,6]
            return [nums[dif[n]], nums[i]] # modificación para salida con valores [11,-1]
    return [] # retorno en caso de no encontrar match

array_de_ejemplo = [3, 5, -4, 8, 11, 1, -1, 6]
suma_objetivo = 10
twoSum(array_de_ejemplo, suma_objetivo) # retorna índices de los valores que hacen match

#%% Batería de tests
arr_test_1 = [3, 5, -4, 8, 11, 1, -1, 6]
arr_test_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
arr_test_3 = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
test_dict = {
    "1": (arr_test_1, 10),
    "2": (arr_test_1, 20),
    "3": ([4, 6], 10),
    "4": ([4, 6, 1], 5), 
    "5": ([4, 6, 1, -3], 3), 
    "6": ([1, 2, 3, 4, 5, 6, 7, 8, 9], 17), 
    "7": (arr_test_2, 18),
    "8": ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18),
    "9": ([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5),
    "10":(arr_test_3, 163),
    "11":(arr_test_3, 164), 
    "12":([3, 5, -4, 8, 11, 1, -1, 6], 15),
    "13":([14], 15),
    "14":([15], 15)
}
def bateriaTests():
    for k in test_dict:
        # pasaTest = False
        tupla = test_dict[k]
        lista = tupla[0]
        target = tupla[1]
        # res = sumarDosNumeros(lista, target)
        # res = sumarDosNumeros2(lista, target)
        # res = sumarDosNumeros3(lista, target)
        # res = sumaDos(lista, target)
        res = twoSum(lista, target)
        print(k, lista, target, "Resultado:", res)

bateriaTests()

# To do: anotar todos los resultados para estos inputs y 
# validar en tests