"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def sol(r,c,size):
            # cheak squre has same value 
            same = True
            for i in range (r, r + size):
                for j in range(c , c + size):
                    if grid[i][j] != grid[r][c]:
                        same = False 
                        break 
                if not same:
                    break
            # if all values are same 
            if same:
                return Node(grid[r][c] == 1, True)
            #divide in to 4 part 
            half = size // 2
            tl = sol(r,c,half)
            tr = sol(r,c+ half,half)
            bl = sol(r + half,c,half)
            br = sol(r + half,c + half, half)
            return Node(
                True,
                False,
                tl,
                tr,
                bl,
                br
            )
        return sol(0,0,len(grid))
