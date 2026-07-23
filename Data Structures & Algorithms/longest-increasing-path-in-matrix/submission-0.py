class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}
        rowLen,colLen=len(matrix),len(matrix[0])
        dir=[(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            res=-float("infinity")
            for rd,cd in dir:
                row,col=rd+i,cd+j
                if row in range(rowLen) and col in range(colLen):
                    if matrix[row][col]>matrix[i][j]:
                        res=max(res,dfs(row,col))
            final=max(res,0)
            dp[(i,j)]=final+1
            return dp[(i,j)]

        maxLen=0
        for i, row in enumerate(matrix):
            for j,col in enumerate(row):
                maxLen=max(maxLen, dfs(i,j))
        return maxLen
                
        




            
        