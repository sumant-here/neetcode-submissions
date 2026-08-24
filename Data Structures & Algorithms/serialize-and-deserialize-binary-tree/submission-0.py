# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        re = []
        def sol1 (node):
            if not node:
                re.append("null")
                return
            re.append(str(node.val))
            sol1(node.left)
            sol1(node.right)
        sol1(root)
        return ",".join(re) # list ru baharo kiribo 

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(",") # puni thore list boneibo 
        ind = 0 # list track rakhiba 
        def sol1():
            nonlocal ind
            if val[ind] == "null":
                ind += 1
                return None
            node = TreeNode(int(val[ind]))
            ind += 1
            node.left = sol1()
            node.right = sol1()
            return node
        return sol1()
