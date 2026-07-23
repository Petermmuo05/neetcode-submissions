# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        inorder=[]
        def dfs(node):
            nonlocal inorder
            if not node:
                inorder.append("N")
                return None
            inorder.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(",".join(inorder))
        return ",".join(inorder)
        


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes=data.split(",")
        index=0
        def dfs():
            nonlocal nodes
            nonlocal index
            if nodes[index]=="N":
                index+=1
                return None
            root=TreeNode(int(nodes[index]))
            index+=1
            root.left=dfs()
            root.right=dfs()
            return root
        return dfs()
