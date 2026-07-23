class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited=set()
        def dfs(row, col):
            print(row, col, visited)
            if (row, col) not in visited:
                visited.add((row,col))
                if board[row][col]=="O":
                    board[row][col]="O#"
            dir=((0,1),(0,-1), (1,0), (-1,0))
            for r,c in dir:
                newRow,newCol=r+row, c+col
                if newRow in range(len(board)) and newCol in range(len(board[0])):
                    if board[newRow][newCol]=="O":
                        dfs(newRow, newCol)

        for row in range(0,len(board)):
            for col in [0, len(board[0])-1]:
                print(row, col)
                if board[row][col]=="O":
                    dfs(row, col)
        for row in [0,len(board)-1]:
            for col in range(0, len(board[0])):
                print(row, col)
                if board[row][col]=="O":
                    dfs(row, col)
            
        print(board)
        for row in range(len(board)):
            for col in range(len(board[0])):

                if board[row][col]=="O#":
                    board[row][col]="O"
                elif board[row][col]=="O":
                    board[row][col]="X"
