class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        safe = [[0 for _ in range(cols)] for _ in range(rows)]
        def dfs(r,c):
            if safe[r][c] == 1:
                return 
            safe[r][c] = 1
            direction = [(-1,0),(0,-1),(1,0),(0,1)]
            for dr , dc in direction:
                nr = r + dr 
                nc = c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if board[nr][nc] == "X":
                    continue
                dfs(nr,nc)
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
        for c in range(cols):
            if board[rows-1][c] == "O":
                dfs(rows-1,c)
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0)
        for r in range(rows):
            if board[r][cols-1] == "O":
                dfs(r,cols-1)
        # change O to x now 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and safe[r][c] == 0:
                    board[r][c] = "X"
        