# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        #swap left and right
        root.left,root.right = root.right,root.left
        #invert left subtree
        self.invertTree(root.left)
        #invert right subtree
        self.invertTree(root.right)
        return root
        