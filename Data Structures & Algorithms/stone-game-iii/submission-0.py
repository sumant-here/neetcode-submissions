class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n+1)
        for i in range(n-1,-1,-1):
            currsum = 0 
            best = float("-inf")
            #current player can take  1 , 2 ,3 stones 
            for j in range(i,min(i+3,n)):
                currsum += stoneValue[j]
                curr = currsum - dp[j+1]
                best = max(best,curr)
            dp[i] = best
        if dp[0] > 0 :
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
        