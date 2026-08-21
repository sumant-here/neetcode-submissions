# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxvalue):
            if node is None:
                return 0 
            count = 0
            # check if current node is good 
            if node.val >= maxvalue:
                count = 1
                maxvalue = node.val
            #check left and right 
            count += dfs(node.left,maxvalue)
            count += dfs(node.right,maxvalue)
            return count
        return dfs(root,root.val)
        