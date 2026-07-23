class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited=set()
        nodes={}
        def dfs(node):
            que=collections.deque()
            que.append((node,None))
            print(nodes)
            while que:
                curNode,parent=que.pop()
                print(curNode, parent)
                for neighbor in nodes[curNode]:
                    if neighbor in visited and neighbor!=parent:
                        print("cycle found")
                        return False
                    if neighbor not in visited:
                        que.append((neighbor, curNode))
                visited.add(curNode)
            return True
                
        for node, neighbor in edges:
            nodes[node]=nodes.get(node,[])+[neighbor]
            nodes[neighbor]=nodes.get(neighbor,[])+[node]
        for node in range(n):
            nodes[node]=nodes.get(node,[])

        if len(edges)!= n-1:
            return False
            print("wrong length")

        if len(edges)!=0:
            if not dfs(0):
                return False
        if n==1 and len(edges)==0:
            return True
        if len(visited)!=n:
            print(visited)
            print("not connected")
            return False
        
        return True

            
