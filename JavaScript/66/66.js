

/**
 * @param {number[]} digits
 * @return {number[]}
 */
let plusOne = function(digits) {
    const length_of_array = digits.length-1
    let count = 0
    while (true){
        if (count === length_of_array+1){
            digits.unshift(1)
            break
        }
        if (digits[length_of_array-count] !== 9){
            digits[length_of_array-count]++
            break
        }
        if (digits[length_of_array-count] === 9){
            digits[length_of_array-count] = 0
        }
        count++
    }
    return digits
};

const array = [9,9,9,9]
console.log(plusOne(array))