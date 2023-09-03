function createCounter(init) {
    var currentVal = init;
    console.log(init);
    console.log(currentVal);
    return {
        increment: function () { return currentVal += 1; },
        decrement: function () { return currentVal -= 1; },
        reset: function () { return currentVal = init; },
    };
}
;
var counter = createCounter(5);
console.log(counter.increment()); // 6
counter.reset(); // 5
counter.decrement(); // 4
