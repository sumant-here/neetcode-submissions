# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: # remember to put root not node
            return 0
        #depth of left subtree
        left = self.maxDepth(root.left)
        #depth of right subtree
        right = self.maxDepth(root.right)
        return 1 + max(left,right)
        