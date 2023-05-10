# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def longestCommonPrefix(strs: list[str]) -> str:
    if not strs: return ""
    common = strs[0]
    for word in strs:
        i = 0
        if len(word) < len(common): common = common[:len(word)]
        for char in word:
            if i >= len(common): break
            if not common: return ""
            if common[i] != char:
                common = common[:i]
                break
            i+=1

    return common


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    strs = ["ab","aa","aaa"]
    print(longestCommonPrefix(strs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
