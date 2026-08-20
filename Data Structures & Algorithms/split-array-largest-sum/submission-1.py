class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left+right)//2
            #chek how many subarry needed
            subarrays = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > mid:
                    subarrays += 1
                    current_sum = num 
                else:
                    current_sum += num
            #we used too many subarrays 
            if subarrays > k :
                left = mid + 1
            #we can split using k or fewer subarry
            else:
                right = mid - 1
        return left
        