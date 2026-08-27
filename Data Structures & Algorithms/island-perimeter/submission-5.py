class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r == 0 or grid[r-1][c] == 0:
                        perimeter += 1
                    if r == rows - 1  or grid[r+1][c] == 0:
                        perimeter +=1
                    if c == 0 or grid[r][c-1] ==0:
                        perimeter += 1
                    if c == cols-1 or grid[r][c+1] == 0:
                        perimeter += 1
        return perimeter
