class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validColumn(i,j, val):
            for rowIndex,row in enumerate(board):
                if rowIndex==i:
                    continue
                if row[j]==val:
                    return False
            return True
        def validRow(i,j, val):
            for colIndex, col in enumerate(board[i]):
                if colIndex==j:
                    continue
                if col==val:
                    return False
            return True
        def validBox(i,j, val):
            startRow=(i//3)*3
            startCol=(j//3)*3
            for rowIndex in range(startRow,startRow+3):
                for colIndex in range(startCol, startCol+3):
                    if (rowIndex,colIndex)==(i,j):
                        continue
                    if board[rowIndex][colIndex]==val:
                        return False
            return True
        for rowIndex in range(9):
            for colIndex in range(9):
                val=board[rowIndex][colIndex]
                if board[rowIndex][colIndex]==".":
                    continue
                if not validRow(rowIndex, colIndex, val) or not validColumn(rowIndex, colIndex, val) or not validBox(rowIndex, colIndex, val):
                    return False
        return True

