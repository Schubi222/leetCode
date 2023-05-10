# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def lengthOfLastWord( s: str) -> int:
    stripped = s.strip()
    split = stripped.split(" ")
    return len(split[-1])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "moon"
    print(lengthOfLastWord(s))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
