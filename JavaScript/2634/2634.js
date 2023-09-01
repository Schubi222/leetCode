/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let retVal = []
    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)){
            retVal.push(arr[i])
        }
    }
    return retVal
};