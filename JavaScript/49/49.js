function groupAnagrams(strs) {
    var retArray = [[]];
    var firstArray = [];
    for (var _i = 0, strs_1 = strs; _i < strs_1.length; _i++) {
        var strElem = strs_1[_i];
        var sortedString = strElem.split('').sort().join('');
        console.log(sortedString, strElem);
        if (retArray[0].length === 0) {
            retArray[0][0] = strElem;
            firstArray.push(sortedString);
            continue;
        }
        for (var i = 0; i < retArray.length; i++) {
            console.log("2.5", strElem, firstArray, retArray);
            if (firstArray[i] === sortedString) {
                retArray[i].push(strElem);
                break;
            }
            console.log("3", strElem, firstArray, retArray);
            if (i === retArray.length - 1) {
                retArray.push(new Array(strElem));
                firstArray.push(sortedString);
                break;
            }
            console.log("4", strElem, firstArray, retArray);
        }
    }
    return retArray;
}
;
var strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"];
console.log(groupAnagrams(strs1));
