# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        temp = ListNode()
        res = temp
        tot = carr = 0
        while l1 or l2 or carr:
            tot = carr
            if l1:
                tot += l1.val
                l1 = l1.next
            if l2:
                tot += l2.val
                l2 = l2.next
            num = tot % 10
            carr = tot // 10
            temp.next = ListNode(num)
            temp = temp.next
        return res.next