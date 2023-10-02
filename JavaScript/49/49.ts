function groupAnagrams(strs: string[]): string[][] {
    let retArray = [[]]
    let firstArray = []
    for (const strElem of strs) {
        const sortedString = strElem.split('').sort().join('')
        if (retArray[0].length === 0){
            retArray[0][0] = strElem;
            firstArray.push(sortedString)
            continue
        }

        for (let i = 0; i < retArray.length; i++) {
            if( firstArray[i] === sortedString){
                retArray[i].push(strElem);
                break
            }
            if (i === retArray.length-1){
                retArray.push(new Array(strElem));
                firstArray.push(sortedString)
                break
            }
        }
    }
    return retArray
};
const strs1 = ["eat","tea","tan","ate","nat","bat"]
console.log(groupAnagrams(strs1))