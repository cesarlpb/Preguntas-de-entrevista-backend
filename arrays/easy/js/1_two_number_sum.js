// Ej. Pasamos la sol 3 a JS

function sumarDosNumeros3(arr, target){
    arr.sort(function(a, b){return a - b});
    let izq = 0, suma;
    der = arr.length - 1;
    while(izq < der){
        suma = arr[izq] + arr[der]
        if(suma === target){
            return [arr[izq], arr[der]]
        } 
        else if (suma < target){ izq++; } 
        else if (suma > target){ der--; }
    }
    return []
}
array_de_ejemplo1 = [3, 5, -4, 8, 11, 1, -1, 6]
suma_objetivo1 = 10
array_de_ejemplo2 = [3, 5, -4, 8, 11, 1, -1, 6]
suma_objetivo2 = 20
sumarDosNumeros3(array_de_ejemplo1, suma_objetivo1) // [-1, 11]
sumarDosNumeros3(array_de_ejemplo2, suma_objetivo2) // []