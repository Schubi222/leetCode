/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    let ans = []
    for (let i = 0; i < n+1; i++) {
        let num = i
        let ones = 0
        while (num > 0){
            if(num % 2 === 1){
                ones++
            }
            num = Math.floor(num/2)
        }
        ans.push(ones)
    }

    return ans
};


console.log(countBits(5))