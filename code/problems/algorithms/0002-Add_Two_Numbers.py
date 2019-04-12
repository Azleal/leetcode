# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = l1
        zeroNode = ListNode(0)
        while l1 != None or l2 != None:
            l1, l2 = (l2, l1) if l1 is None else (l1, l2)
            l2 = zeroNode if l2 is None else l2

            div, mod = (l1.val + l2.val) // 10, (l1.val + l2.val) % 10
            l1.val = mod
            l1.next, l2.next = (l1.next, l2.next) if l1.next is not None else (l2.next, l1.next)

            if l1.next != None:
                l1.next.val += div
            elif div > 0:
                l1.next = ListNode(div)
            l1, l2 = l1.next, l2.next
        return r


# l1 = ListNode(2)
# # l1.next=ListNode(4)
# # l1.next.next=ListNode(3)
# #
# # l2 = ListNode(5)
# # l2.next=ListNode(6)
# # l2.next.next=ListNode(4)

l1 = ListNode(0)

l2 = ListNode(7)
l2.next=ListNode(3)

r=Solution().addTwoNumbers(l1,l2)
print(r)

