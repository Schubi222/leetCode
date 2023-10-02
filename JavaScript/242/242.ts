function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false
    for (const sElement of s) {
        if (t.length === 0){return false}
        const oldT =t
        t=t.replace(sElement,'')
        if (oldT.length===t.length) {
            return false
        }
    }
    return t === '';
};

console.log(isAnagram( "anagran", "nagaram"))