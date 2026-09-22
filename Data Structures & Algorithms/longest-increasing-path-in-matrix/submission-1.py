class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp =[[1 for _ in range(n)] for _ in range(m)] #bcz for 1 elemnt 1 
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((matrix[i][j],i,j))
        cells.sort() #sort cells by their values
        answer = 1
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        for value, i, j in cells:
            for di, dj in directions:
                ni = i + di 
                nj = j + dj 
                if (0 <= ni < m and 0 <= nj <n and matrix[ni][nj] < value):
                    dp[i][j] = max(dp[i][j], 1 +dp[ni][nj])
            answer = max(answer,dp[i][j])
        return answer 

