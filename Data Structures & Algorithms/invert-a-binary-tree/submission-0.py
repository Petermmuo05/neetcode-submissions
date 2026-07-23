# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertKids(node):
            if node:
                left, right=node.left, node.right
                node.left, node.right=right, left
                invertKids(node.left)
                invertKids(node.right)
        invertKids(root)
        return root

        