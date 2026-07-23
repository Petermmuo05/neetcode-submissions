class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        sets=[set(), set()]

        def dfs(pos, setIndex):
            i,j=pos
            rowlen,collen=len(heights),len(heights[0])
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            que=collections.deque()
            que.append(pos)
            while que:
                row,col=que.pop()
                for rd,cd in directions:
                    r,c=row+rd,col+cd
                    if r in range(rowlen) and c in range(collen):
                        if heights[r][c]>=heights[row][col] and (r,c) not in sets[setIndex]:
                            sets[setIndex].add((r,c))
                            que.append((r,c))

        for i in range(len(heights[0])):
            sets[0].add((0,i))
            dfs((0,i),0)
            sets[1].add((len(heights)-1,i))
            dfs((len(heights)-1,i),1)

        for j in range(len(heights)):
            sets[0].add((j,0))
            dfs((j,0),0)
            sets[1].add((j,len(heights[0])-1))
            dfs((j,len(heights[0])-1),1)
        
        pacific=sets[0]
        atlantic=sets[1]
        print(pacific, atlantic)
        result=pacific.intersection(atlantic)
        return [list(pos) for pos in result]
        


                