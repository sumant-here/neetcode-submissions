# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if subroot is empty the it always subtree
        if subRoot is None:
            return True
        #if root become empty but subroot is not
        if root is None:
            return False
        #cheak if tree are smae at c node
        if self.isSameTree(root,subRoot):
            return True
        #search in left or right subtree
        return(
            self.isSubtree(root.left,subRoot)
            or
            self.isSubtree(root.right,subRoot)
        )
    def isSameTree(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return(
            self.isSameTree(p.left,q.left)
            and
            self.isSameTree(p.right,q.right)
        )

        #here i have applied two logig 1 when the root is tarat and 2nd where the after getting the root i need to match the values in it which is issame tree
        