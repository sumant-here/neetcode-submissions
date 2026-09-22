class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        #impossible case
        if total < abs(target):
            return 0 
        if (total+target) % 2 != 0 :
            return 0
        required = (total + target) // 2
        n = len(nums)
        dp = [[0 for _ in range(required+1)] for _ in range(n+1)]
        #there is 1 way to make the sum is zero 
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(required +1):
                # dont take numes[i-1] i got it same qn
                not_take = dp[i-1][j]
                #take nums[i-1]
                take = 0 
                if nums[i-1] <= j :
                    take = dp[i-1][j-nums[i-1]]
                dp[i][j] = take + not_take
        return dp[n][required]
        