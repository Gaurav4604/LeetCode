class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def createListNode(self, target: list, index = 0):
        if (index != len(target)):
            return ListNode(val=target[index], next=self.createListNode(target, index + 1))

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        str_l1 = ""
        str_l2 = ""
        while (l1.next):
            str_l1 += str(l1.val)
            l1 = l1.next
        str_l1 += str(l1.val)
        str_l1 = int(str_l1[::-1])

        while (l2.next):
            str_l2 += str(l2.val)
            l2 = l2.next
        str_l2 += str(l2.val)
        str_l2 = int(str_l2[::-1])
        num = str_l1+str_l2
        return self.createListNode(target=[int(x) for x in str(num)][::-1])
# nodes = ListNode(val=1, next= ListNode(val=0, next = ListNode(val=3)))

# print(nodes.val)
s = Solution()
l1 = s.createListNode([2, 4, 3])
l2 = s.createListNode([5, 6, 4])
print(s.addTwoNumbers(l1, l2).val)
print(s.addTwoNumbers(l1, l2).next.val)
print(s.addTwoNumbers(l1, l2).next.next.val)