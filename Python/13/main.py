# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def romanToInt(s: str) -> int:
    translation = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    numb = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        numb += translation[char]
    return numb

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(romanToInt('MIMCXV'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
