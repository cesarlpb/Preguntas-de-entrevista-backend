// Ej Pasar sol 2 a JS

function es_subarr_valido2(arr, sub_arr){
    let i = 0, j = 0;
    while(i < arr.length && j < sub_arr.length){
        if( arr[i] === sub_arr[j] ){
            j++;
        }
        i++;
    }
    return j === sub_arr.length
}

let arr = [1, 2, 3, 4], sub_arr = [1, 3, 4];
let arr2 = [1, 2, 3, 4], sub_arr2 = [2, 4] 
let arr3 = [1, 2, 3, 4], sub_arr3 = [4, 1]

es_subarr_valido2(arr, sub_arr)   // True
es_subarr_valido2(arr2, sub_arr2) // True
es_subarr_valido2(arr3, sub_arr3) // False
es_subarr_valido2([1, 2, 3, 4, 1], [1, 4, 1]) // True