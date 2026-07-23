class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited=[]
        nodes={}
        order=[]
        def dfs(node,path):
            visited.append(node)
            if node in path:
                return False
            isNotCycle=True
            for neighbor in nodes[node]:
               if not dfs(neighbor,path+[node]):
                isNotCycle=False
            if node not in order:
                order.append(node)
            return isNotCycle
        for node,neighbor in prerequisites:
            nodes[node]=nodes.get(node,[])+[neighbor]
        for node in range(numCourses):
            nodes[node]=nodes.get(node,[])
        for node in nodes:
            if node not in visited:
                if not dfs(node,[]):
                    return []
        return order
        
        

            