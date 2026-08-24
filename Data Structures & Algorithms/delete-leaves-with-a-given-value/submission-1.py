# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        #first solve left subtree
        root.left = self.removeLeafNodes(root.left,target)
        #then solve right subtree
        root.right = self.removeLeafNodes(root.right,target)
        #now cheak current Node
        if root.val == target and root.left is None and root.right is None:
            return None
        return root

        