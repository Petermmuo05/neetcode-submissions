# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=[]
        res=[]
        if root:
            queue.append(root)
            res.append([root.val])
        while not len(queue)==0:
            curr=[]
            for node in queue:
                if node:
                    curr.append(node.left)
                    curr.append(node.right),
            if [node.val for node in curr if node]!=[]:
                res.append([node.val for node in curr if node])
                queue=curr
            else:
                queue=[]
        return res



