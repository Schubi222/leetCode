function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    for (let i = 0; i < arr.length; i++) {
        arr[i] = fn(arr[i],i)
    }
    return arr
};

const arr = [1,2,3]
function plusone(n) { return n + 1; }

const newArray = map(arr, plusone); // [2,3,4]
console.log(newArray)