# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        firstTree=""
        secondTree=""
        isFirst=True
        def dfs(node):
            nonlocal firstTree
            nonlocal secondTree
            if isFirst:
                if node:
                    firstTree+=str(node.val)
                else:
                    firstTree+="_"
            else:
                if node:
                    secondTree+=str(node.val)
                else:
                    secondTree+="_"
            if node:
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        isFirst=False
        dfs(subRoot)
        return secondTree in firstTree