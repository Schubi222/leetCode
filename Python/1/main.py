# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def twoSum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i in range(len(nums)):
        rest = target - nums[i]
        if rest in hashmap:
            return [hashmap[rest],i]
        hashmap[nums[i]] = i
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    print(twoSum(nums, target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
