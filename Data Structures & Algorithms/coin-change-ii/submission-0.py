class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp =[[0 for _ in range(amount+1)]for _ in range(n+1)]
        #amount 0 always be made in exactyly 1 way
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for target in range(1,amount+1):
                # dosnt take the current coin 
                not_take = dp[i-1][target]
                #takek current coin 
                take = 0 
                if coins[i-1] <= target:
                    take = dp[i][target-coins[i-1]]
                dp[i][target] = not_take + take 
        return dp[n][amount]
        