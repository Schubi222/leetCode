function map(arr, fn) {
    for (var i = 0; i < arr.length; i++) {
        arr[i] = fn(arr[i], i);
    }
    return arr;
}
;
var arr = [1, 2, 3];
function plusone(n) { return n + 1; }
var newArray = map(arr, plusone); // [2,3,4]
console.log(newArray);
