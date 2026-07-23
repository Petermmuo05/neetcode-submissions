class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isRowValid(row):
            vals=[]
            for val in board[row]:
                print(val, board[row], "row")
                if val==".":
                    continue
                val=int(val)
                if val not in range(1,10) or val in vals:
                    print(row, "row")
                    return False
                vals.append(val)
            return True
        def isColValid(col):
            vals=[]
            for row in board:
                val=row[col]
                if val==".":
                    continue
                val=int(val)
                if val not in range(1,10) or val in vals:
                    print(col, "col")
                    return False
                vals.append(val)
            return True
        def isBoardValid(row, col):
            row*=3
            col*=3
            vals=[]
            for row in board[row:row+3]:
                for val in row[col:col+3]:
                    if val==".":
                        continue
                    if val in vals:
                        print((row, col), "box")
                        return False
                    vals.append(val)
            return True
        for i in range(9):
            if not isRowValid(i) or not isColValid(i):
                return False
        for i in range(3):
            for j in range(3):
                if not isBoardValid(i,j):
                    return False
        return True


