class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=[]
        nodes={}
        def dfs(node):
            path=[]
            que=collections.deque()
            que.append(node)
            while que:
                print(nodes)
                cur=que.pop()
                print(cur)
                if cur not in nodes:
                    return True
                neighbors=nodes[cur]
                for neighbor in neighbors:
                    if neighbor in path:
                        return False
                    que.append(neighbor)
                visited.append(cur)
                path.append(cur)
        for node,neighbor in prerequisites:
            nodes[node]=nodes.get(node,[])+[neighbor]
        for node in nodes:
            if node not in visited:
                if not dfs(node):
                    return False
        return True



                

            
