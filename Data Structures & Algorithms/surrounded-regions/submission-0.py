class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited=[]
        cur=[]
        def bfs(pos):
            que=collections.deque()
            rowLen,colLen=len(board),len(board[0])
            directions=[(0,1),(0,-1),(1,0),(-1,0)]
            que.append(pos)
            isSurrounded=True
            while que:
                i,j=que.popleft()
                for rd,cd in directions:
                    r,c=i+rd,j+cd
                    if r in range(rowLen) and c in range(colLen):
                        if board[r][c]=="O" and (r,c) not in visited:
                            visited.append((r,c))
                            cur.append((r,c))
                            if r in [0,rowLen-1] or c in [0,colLen-1]:
                                isSurrounded=False
                            que.append((r,c))
            return isSurrounded
        
        if len(board)<3 or len(board[0])<3:
            return 
        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if board[i][j]=="O" and (i,j) not in visited:
                    visited.append((i,j))
                    cur.append((i,j))
                    if bfs((i,j)):
                        print(cur,visited)
                        for row,col in cur:
                            board[row][col]="X"
                    cur=[]
                







                

