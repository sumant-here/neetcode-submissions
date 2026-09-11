import heapq
from typing import List 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #actully we want heavy weight . but probabbly it will be on last there for we manke it negative so that . it will come first . as we did in min heap and we have to represent that  - in to + 
        heap = [-stone for stone in stones]
        heapq.heapify(heap) #the internal arrangement satisfies the min-heap property
        while len(heap) > 1 :
            y = - heapq.heappop(heap) # we put - bcz we want 2 make it + 
            x = - heapq.heappop(heap)
            if y != x:
                heapq.heappush(heap, -(y - x))
        return -heap[0] if heap else 0 
        
