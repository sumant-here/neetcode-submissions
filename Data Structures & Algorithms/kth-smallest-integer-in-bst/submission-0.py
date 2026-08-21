# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0 
        answer = 0 
        def inorder(node):
            nonlocal count,answer
            if node is None:
                return
            # go Left 
            inorder(node.left)
            #visit current node
            count += 1
            if count == k :
                answer = node.val
                return
            # go right 
            inorder(node.right)
        inorder(root)
        return answer 
        