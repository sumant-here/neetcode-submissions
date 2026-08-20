# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        for _ in range(k):
            if temp is None:
                return head
            temp = temp.next
        #reverse K nodes
        prev = None
        curr  = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head.next = self.reverseKGroup(curr,k)
        return prev
        