# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        firstTree=[]
        secondTree=[]
        isFirst=True
        def dfs(node):
            if isFirst:
                if node:
                    firstTree.append(node.val)
                else:
                    firstTree.append(None)
            else:
                if node:
                    secondTree.append(node.val)
                else:
                    secondTree.append(None) 
            if node:   
                dfs(node.left)
                dfs(node.right)

        dfs(p)
        isFirst=False
        dfs(q)
        return firstTree==secondTree

