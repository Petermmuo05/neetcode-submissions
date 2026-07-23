# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        curMax=-float("inf")
        def maxPath(node):
            nonlocal curMax
            if not node:
                return 0
            print(curMax, node.val)
            left=maxPath(node.left)
            right=maxPath(node.right)
            print(curMax, node.val,node.val+left,node.val+right,node.val+left+right)
            curMax=max(curMax, node.val,node.val+left,node.val+right,node.val+left+right)
            return max(node.val,node.val+left,node.val+right)
        maxPath(root)
        return curMax

        
        