# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #node not found
        if root is None:
            return None
        # search in left subtree
        if key < root.val:
            root.left =self.deleteNode(root.left,key)
        # search right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        #found the node which we wanr to delete 
        else:
            # calse 1 no left child 
            if root.left is None:
                return root.right
            #case 2 no right child
            if root.right is None:
                return root.left
            #case 3 two child
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(
                root.right,
                successor.val
            )
        return root 

        