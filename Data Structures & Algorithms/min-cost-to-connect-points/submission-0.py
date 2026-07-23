class Solution:
    class Ufs:
        def __init__(self,points):
            self.parents={node:node for node in points}
            self.rank={node:0 for node in points}

        def find(self,node):
            if self.parents[node]==node:
                return node
            self.parents[node]=self.find(self.parents[node])
            return self.parents[node]
        def union(self,u,v):
            pu=self.find(u)
            pv=self.find(v)
            if pu==pv:
                return False
            if self.rank[pu]<self.rank[pv]:
                self.parents[pu]=pv
            elif self.rank[pv]<self.rank[pu]:
                self.parents[pv]=pu
            else:
                self.parents[pv]=pu
                self.rank[pu]+=1
            return True

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph=[]
        points=[tuple(node) for node in points]
        for point1 in points:
            for point2 in points:
                if point1!=point2:
                    x1,y1=point1
                    x2,y2=point2
                    weight=abs(x1-x2)+abs(y1-y2)
                    graph.append((point1,point2,weight))
        sorted_edges = sorted(graph, key=lambda x: x[2])
        result_weight=0
        node_count=0
        ufs=self.Ufs(points)
        for u,v,weight in sorted_edges:
            if ufs.union(u,v):
                result_weight+=weight
                node_count+=1
                if node_count==len(graph)-1:
                    break
        return result_weight




        

