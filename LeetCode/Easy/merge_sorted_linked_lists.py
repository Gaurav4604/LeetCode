class ListNode:
    def __init__(self, val=0, next=None):
        self.val:int = val
        self.next = next

def create(nums:list, index = 0):
    if index != len(nums):
        return ListNode(val = nums[index], next = create(nums, index=index +1))
        



class Solution:
    def mergeTwoLists(l1, l2):
        l1 = create(l1)
        l2 = create(l2)
        l3 = []
        
        while (l1 != None and l2 != None):
            if l2.val >= l1.val:
                l3.append(l1.val)
                l1 = l1.next
            else:
                l3.append(l2.val)
                l2 = l2.next
            print(l3)

        
        if l1 != None:
            while l1 != None:
                l3.append(l1.val)
                l1 = l1.next
        elif l2 != None:
            while l2 != None:
                l3.append(l2.val)
                l2 = l2.next
        
        print(l3)



s = Solution
s.mergeTwoLists([-9,3], [5,7])

