# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # prev = None
        # def inroder(node):
        #     nonlocal prev
        #     if node is None:
        #         return True
        #     # go left
        #     if not inroder(node.left):
        #         return False
        #     # check current node
        #     if prev is not None and node.val <= prev:
        #         return False
        #     prev = node.val
        #     # go right
        #     return inorder(node.right)
        # return inorder(root)
        def dfs(node,low,high):
            if node is None:
                return True
            if node.val <= low or node.val >= high:
                return False 
            return(
                dfs(node.left,low,node.val)
                and 
                dfs(node.right,node.val,high)

            )
        return dfs(root,float("-inf"),float("inf"))
        