type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): ReturnObj {
    let currentVal = init
    return {
        increment: () => currentVal+=1,
        decrement: () => currentVal-=1,
        reset: () => currentVal = init,
    }
};


const counter = createCounter(5)
console.log(counter.increment()); // 6
counter.reset(); // 5
counter.decrement(); // 4
