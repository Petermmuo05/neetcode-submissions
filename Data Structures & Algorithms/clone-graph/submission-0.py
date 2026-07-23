"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        def dfs(node,hashmap):
            if node in hashmap:
                return
            new_node=Node(node.val)
            hashmap[node]=new_node
            for neighbor in node.neighbors:
                dfs(neighbor, hashmap)
                hashmap[node].neighbors.append(hashmap[neighbor])
        hashmap={}
        firstNode=Node(1)
        hashmap[node]=firstNode
        for neighbor in node.neighbors:
            dfs(neighbor, hashmap)
            hashmap[node].neighbors.append(hashmap[neighbor])
        return firstNode

        
            

                



            
        