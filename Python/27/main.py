# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def removeElement( nums: list[int], val: int) -> int:
    if not nums: return 0
    if val not in nums: return len(nums)
    while val in nums:
        nums.remove(val)
    return len(nums)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,1]
    val = 2
    print(removeElement(nums, val), nums)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
