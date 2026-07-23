class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components=0
        visited=set()
        nodes={}
        def dfs(node):
            path=set()
            que=collections.deque()
            que.append((node, None))
            while que:
                curNode,parent=que.pop()
                for neighbor in nodes[curNode]:
                    if not (neighbor in path and neighbor!=parent):
                        print("not forming cycle")
                        if neighbor not in path:
                            que.append((neighbor,curNode))
                visited.add(curNode)
                path.add(curNode)

        for node, neighbor in edges:
            nodes[node]=nodes.get(node,[])+[neighbor]
            nodes[neighbor]=nodes.get(neighbor,[])+[node]
        for node in range(n):
            nodes[node]=nodes.get(node,[])
            if node not in visited:
                dfs(node)
                components+=1
        return components
                

                                



            
