# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #both node are empty
        if p is None and q is None:
            return True
        #one is empty other is not
        if p is None or q is None:
            return False
        #values are diff
        if p.val != q.val:
            return False
        #cheak left and right subtrees
        return(
            self.isSameTree(p.left,q.left)
            and
            self.isSameTree(p.right,q.right)
        )
        