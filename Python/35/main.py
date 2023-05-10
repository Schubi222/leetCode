# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def searchInsert( nums: list[int], target: int) -> int:

    itcount = 2
    numslen = len(nums)-1
    lenn = round(numslen/2)
    while 1:

        if nums[0] >= target: return 0
        if nums[numslen] < target: return numslen+1
        if nums[numslen] == target: return numslen

        #if lenn == 0: return lenn
        if lenn == numslen : return lenn
        if nums[lenn] == target: return lenn
        if nums[lenn - 1] < target < nums[lenn]: return lenn
        if nums[lenn] < target < nums[lenn+1]: return lenn+1
        if nums[lenn] < target:
            lenn = lenn + round(numslen/(2*itcount))
            itcount+=1
            continue
        if nums[lenn] > target:
            lenn = lenn - round(numslen/(2*itcount))
            itcount += 1
            continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,3]
    target = 3
    print(searchInsert(nums, target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
