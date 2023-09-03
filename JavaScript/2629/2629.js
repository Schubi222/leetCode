function compose(functions) {
    return function (x) {
        var retval = x;
        for (var i = functions.length; i > 0; i--) {
            retval = functions.pop()(retval);
        }
        return retval;
    };
}
;
var fn = compose([function (x) { return x + 1; }, function (x) { return 2 * x; }]);
console.log(fn(4)); // 9
