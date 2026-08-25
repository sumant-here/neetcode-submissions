# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        du = ListNode(0)
        cu = du
        ca = 0
        while l1 or l2 or ca :
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            to = x + y + ca
            ca = to // 10
            di = to % 10 
            cu.next = ListNode(di)
            cu = cu.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return du.next

        