class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        n = len(stones)
        dp =[[False for _ in range(target+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True 
        for i in range(1,n+1):
            for j in range(1,target+1):
                dp[i][j] = dp[i-1][j]
                if stones[i-1] <= j :
                    dp[i][j] =(dp[i][j] or dp[i-1][j-stones[i-1]])
        for j in range(target, -1,-1):
            if dp[n][j]:
                return total - 2* j
        return 0


        