class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten=collections.deque()
        visited=[]
        def bfs():
            directions=[(0,1),(0,-1),(1,0),(-1,0)]
            rowLen, colLen=len(grid),len(grid[0])
            maxMin=0
            while rotten:
                i,j,min=rotten.popleft()
                for rd,cd in directions:
                    r,c=i+rd,j+cd
                    if r in range(rowLen) and c in range(colLen):
                        if grid[r][c]==1 and (r,c) not in visited:
                            visited.append((r,c))
                            grid[r][c]==2
                            maxMin=max(maxMin,min+1)
                            rotten.append((r,c,min+1))
            return maxMin

        lenFruit=0
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if grid[i][j]!=0:
                    lenFruit+=1
                if grid[i][j]==2:
                    rotten.append((i,j,0))
                    visited.append((i,j))
        result=bfs()
        if len(visited)!=lenFruit:
            return -1
        else:
            return result


                        
