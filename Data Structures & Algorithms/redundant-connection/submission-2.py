class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents=[i for i in range(len(edges)+1)]
        rank=[0]*(len(edges)+1)
        def find(node):
            p=parents[node]
            while p!=parents[p]:
                parents[p]=parents[parents[p]]
                p=parents[p]
            return p
        def union(node1,node2):
            p1,p2=find(node1),find(node2)
            if p1!=p2:
                if rank[p1]>=rank[p2]:
                    parents[p2]=p1
                    rank[p1]+=rank[p2]
                else:
                    parents[p1]=p2
                    rank[p2]+=rank[p1]
                return True
            else:
                return False
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        





            





