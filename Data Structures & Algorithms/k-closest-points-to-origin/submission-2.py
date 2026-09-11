import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x , y in points:
            distance = x*x + y*y 
            heapq.heappush(heap,(-distance,x,y))
            if len(heap) > k :
                heapq.heappop(heap)
        return[[x,y] for distance,x,y in heap]

#  We will store points in the heap.
# But there is an important trick here.
# We want to keep the K smallest distances.
# So we want to remove the largest distance whenever we have more than k points.
# Therefore, we need a max heap.
# But Python only gives us a min heap.
# So we use negative distances