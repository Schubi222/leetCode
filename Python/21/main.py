# This is a sample Python script.
from typing import Optional


# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 and not list2: return list1
    if list2 and not list1: return list2
    if not list1 and not list2: return None

    retlist = Optional[ListNode]

    while True:
        if not list1 and not list2:
            break
        if list1 and list1.val <= (list2.val if list2 else 0):
            retlist.append(list1.val)
            del list1.val
        else:
            retlist.append(list2.val)
            del list2.val

    return retlist

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1_ = [1,2,3]
    list2_ = [1,2,3]
    print(mergeTwoLists(list1_, list2_))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
