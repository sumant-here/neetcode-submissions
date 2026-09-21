class Solution:
    def so(self,nums):
        n = len(nums)
        dp  =[-1] * n 
        dp[0] = nums[0]
        for index in range(1,n):
            if index > 1:
                pick = nums[index]+ dp[index-2]
            else:
                pick = nums[index]
            not_pick = 0 + dp[index-1]
            dp[index] =max(pick,not_pick)
        return dp[n-1]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if  n == 1:
            return nums[0]
        an1  = self.so(nums[0:n-1])
        an2 = self.so(nums[1:n])
        return max(an1,an2)

        