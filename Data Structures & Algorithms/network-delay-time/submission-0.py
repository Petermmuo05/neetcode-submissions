class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph={}
        for node in times:
            u,v,t=node
            neighbors=graph.get(u,{})
            neighbors[v]=t
            graph[u]=neighbors
        distance={node:float("inf") for node in range(1,n+1)}
        distance[k]=0
        pq=[(0,k)]
        visited=set()
        print(graph)
        while pq:
            current_distance,current=heapq.heappop(pq)
            if current in visited:
                continue
            if current not in graph:
                continue
            for neighbor, weight in graph[current].items():
                if neighbor not in visited:
                    new_distance=current_distance+weight
                    if new_distance<distance[neighbor]:
                        distance[neighbor]=new_distance
                        heapq.heappush(pq,(new_distance,neighbor))
        print(distance)
        output=max(list(distance.values()))
        return output if output!=float("inf") else -1



