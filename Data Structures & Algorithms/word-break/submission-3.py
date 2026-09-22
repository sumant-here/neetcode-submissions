class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
         n = len(s)
         dp = [False] * (n+1)
         dp[0] = True
         for i in range(1,n+1):
            for word in wordDict:
                p = len(word)
                if p <=i and dp[i-p]:
                    if s[i-p:i] == word:
                        dp[i]= True
                        break
         return dp[n]
        