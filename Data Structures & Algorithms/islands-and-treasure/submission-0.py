class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def bfs(pos):
            visited=set()
            i,j=pos
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            rowLen, colLen=len(grid), len(grid[0])
            que=collections.deque()
            que.append((i,j,0))
            while que:
                row,col,dist =que.popleft()
                for rd, cd in directions:
                    r,c=row+rd,col+cd
                    if r in range(rowLen) and c in range(colLen):
                        if grid[r][c] not in [0,-1] and (r,c) not in visited:
                            visited.add((r,c))
                            grid[r][c]=min(dist+1, grid[r][c])
                            que.append((r,c, dist+1))
               
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col==0:
                    bfs((i,j))
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col==2147483647:
                    grid[i][j]=-1



        


                    


                