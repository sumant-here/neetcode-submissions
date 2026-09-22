class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp  = [[-1,-1]for _ in range(n+2)]
        #base
        dp[n][0] = 0
        dp[n][1] = 0

        dp[n + 1][0] = 0
        dp[n + 1][1] = 0
        for index in range(n-1,-1,-1):
            for buy in range(0,2):
                if buy == 1:
                    buy_p = -prices[index] + dp[index+1][0]
                    not_buy = 0 + dp[index+1][1]
                    profit = max(buy_p,not_buy)
                else:
                    sell = prices[index] + dp[index+2][1]
                    not_sell = 0 + dp[index+1][0]
                    profit = max(sell,not_sell)
                dp[index][buy] = profit
        return dp[0][1]
        