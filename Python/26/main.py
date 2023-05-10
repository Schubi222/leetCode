# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def removeDuplicates(nums: list[int]) -> int:
    if not len(nums): return 0
    count = 0
    while 1:
        if count == len(nums): break

        if not count and count+1 < len(nums) and nums[count] == nums[count+1]:
            del nums[count+1]
            count -= 1
        elif count - 1 > -1 and nums[count] == nums[count - 1]:
            del nums[count]
            count -= 1

        elif count+1 < len(nums) and nums[count] == nums[count+1]:
            del nums[count+1]
            count -= 1

        count += 1

    return len(nums)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums),nums)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
