# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def isAlienSorted(words: List[str], order: str) -> bool:
    counter = 0
    if len(words) == 1: return True
    while 1:
        if counter+1 == len(words): return True
        wordPointer = 0
        atPointer = words[counter]
        pointerPlus =words[counter+1]
        while len(atPointer) > wordPointer and len(pointerPlus) > wordPointer:
            if order.index(atPointer[wordPointer]) < order.index(pointerPlus[wordPointer]): break
            if order.index(atPointer[wordPointer]) > order.index(pointerPlus[wordPointer]): return False
            wordPointer+=1
        if len(pointerPlus) < len(atPointer) and len(pointerPlus) <= wordPointer: return False
        counter+=1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = ["apple","applea"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print(isAlienSorted(words,order))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
