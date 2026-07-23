class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        islands=0
        def bfs(i,j):
            row, col=len(grid), len(grid[0])
            que=collections.deque()
            que.append((i,j))
            directions=[(1,0), (-1,0), (0,1), (0,-1)]
            while que:
                pr, pc=que.popleft()
                for rd,cd in directions:
                    if pr+rd in range(row) and pc+cd in range(col):
                        r,c=pr+rd,pc+cd
                        if grid[r][c]=="1" and (r,c) not in visited:
                            que.append((r,c))
                            visited.add((r,c))
                        


        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if col=="1" and (i,j) not in visited:
                    visited.add((i,j))
                    bfs(i,j)
                    islands+=1

        return islands
        