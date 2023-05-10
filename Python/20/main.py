# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def isValid( s: str) -> bool:
    openArray = []
    openB = ['(','{','[']

    for c in s:
        if c in openB:
            openArray.append(c)
            continue
        if openArray and ((c == ')' and openArray[-1] == '(') or (c == '}' and openArray[-1] == '{') or (c == ']' and openArray[-1] == '[')):
            del openArray[-1]
        else:
            return False
    if openArray:
        return False
    return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "[([]])"
    print(isValid(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
