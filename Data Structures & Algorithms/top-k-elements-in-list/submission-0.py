from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # Count frequency of each number
        count = Counter(nums)

        # Min heap
        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            # Keep only k elements
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract elements
        result = []

        while heap:
            freq, num = heapq.heappop(heap)
            result.append(num)

        return result
        