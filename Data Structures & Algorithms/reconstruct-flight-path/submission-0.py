class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        res=[]
        def dfs(node):
            print(adj)
            while adj[node]:
                neighbor=adj[node].pop()
                dfs(neighbor)
            res.append(node)
        dfs('JFK')
        return res[::-1]
            

        