type F = (x: number) => number;

function compose(functions: F[]): F {
    return function(x) {
        let retval = x
        for (let i = functions.length; i > 0; i--) {
            retval = functions.pop()(retval)
        }
        return retval
    }
};


const fn = compose([x => x + 1, x => 2 * x])
console.log(fn(4)) // 9
