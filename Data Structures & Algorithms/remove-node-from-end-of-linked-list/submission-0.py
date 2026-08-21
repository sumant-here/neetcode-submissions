# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(0)
        dum.next = head
        slow = dum
        fast = dum
        # move fast n step ahead
        for _ in range(n):
            fast = fast.next
        #move both until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dum.next

        