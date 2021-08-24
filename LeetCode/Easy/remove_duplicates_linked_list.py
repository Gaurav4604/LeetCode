class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def construct(ls:list):
    head = None
    parser = None
    for i in range(len(ls)):
        if head == None:
            head = ListNode(val=ls[i])
            parser = head
            continue
        else:
            parser.next = ListNode(val=ls[i])
            parser = parser.next
    return head

def destruct(head:ListNode):
    ls = []
    while (head != None):
        ls.append(head.val)
        head = head.next
    return ls

def removeDuplicates(ls:list[int]):
    ls = list(set(ls))
    ls.sort()
    return ls

def deleteDuplicates(head):
    ls = destruct(head)
    if len(ls) == 0:
        return None
    else:
        ls = removeDuplicates(ls)
        head = construct(ls)
        return head

head = deleteDuplicates(construct([1,1,2,3,3]))
print(destruct(head))