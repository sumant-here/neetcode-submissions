# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # both nodes are smaller than root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        # both nodes are greater that the roo t
        if p.val > root.val and q.val> root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        # diff side
        # or one of them root
        return root 
        
        # left < root < right thismethod follwessd