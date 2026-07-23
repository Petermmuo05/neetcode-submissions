class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap=[(grid[0][0],0,0)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        y=len(grid)-1
        x=len(grid[-1])-1
        visited=set()
        while minHeap:
            maxHeight,r,c=heapq.heappop(minHeap)
            if r==x and c==y:
                return maxHeight
            visited.add((r,c))
            for rd,cd in directions:
                row,col=r+rd,c+cd
                if row in range(x+1) and col in range(y+1):
                    if (row,col) not in visited:
                        heapq.heappush(minHeap,(max(maxHeight,grid[row][col]),row,col))
            
                        


        