# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        an = float("-inf")
        def solve(node):
            nonlocal an 
            if not node:
                return 0
            left = max(0,solve(node.left))
            right = max(0,solve(node.right))
            #path passing throuugh current node
            cur =  node.val + left + right
            #update global answer 
            an = max(an,cur)
            #give parent the best onse side path 
            return node.val + max(left,right)
        solve(root)
        return an
        