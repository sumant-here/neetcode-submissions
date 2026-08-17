# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        #put the first node of every list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))
        dum = ListNode()
        cur = dum
        while heap:
            value , i , node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
        return dum.next

        