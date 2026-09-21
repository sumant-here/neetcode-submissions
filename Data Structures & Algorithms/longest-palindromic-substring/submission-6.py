class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]* n for _ in range(n)]
        start = 0
        maxLen = 1
        #every signle char is palandrom 
        for i in range(n):
            dp[i][i] = True
        #check cusbrtin 2 or ore 
        for le in range(2,n+1):
            for i in range(n-le + 1):
                j = i + le -1 
                if s[i] == s[j]:
                    if le == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and le > maxLen:
                    start = i
                    maxLen = le
        return s[start:start + maxLen]

        