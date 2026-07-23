class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph={}
        for edge in flights:
            u,v,weight=edge
            neighbors=graph.get(u,{})
            neighbors[v]=weight
            graph[u]=neighbors
        print(graph)
        distance={node:float("infinity") for node in range(n)}
        distance[src]=0
        for _ in range(k+1):
            temp_distance=distance.copy()
            for u in graph:
                for v,weight in graph[u].items():
                    if distance[u]!=float("infinity") and distance[u]+weight<temp_distance[v]:
                        temp_distance[v]=distance[u]+weight
            distance=temp_distance
        return distance[dst] if distance[dst]!=float("infinity") else -1
                        
            
        