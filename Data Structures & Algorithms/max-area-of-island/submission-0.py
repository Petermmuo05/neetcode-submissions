class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea=0
        visited=set()
        def bfs(pos):
            nonlocal maxArea
            area=1
            rowLen, colLen=len(grid), len(grid[0])
            directions=[(-1,0),(1,0),(0,1),(0,-1)]
            que=collections.deque()
            que.append(pos)
            while que:
                i,j=que.popleft()
                for rd,cd in directions:
                    r,c=rd+i,cd+j
                    if r in range(rowLen) and c in range(colLen):
                        if grid[r][c]==1 and (r,c) not in visited:
                            visited.add((r,c))
                            area+=1
                            que.append((r,c))
            maxArea=max(area,maxArea)
            

        for i, row in enumerate(grid):
            for j,col in enumerate(row):
                if col==1 and col not in visited:
                    visited.add((i,j))
                    bfs((i,j))
        return maxArea

                    