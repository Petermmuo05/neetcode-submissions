class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isDone={}
        
        
        colHashNums=[{str(x):True for x in range(1,10)} for _ in range(9)]
        boxHashNums=[[{str(x):True for x in range(1,10)} for _ in range(3)] for _ in range(3)]
        for i in range(0,9):
            rowHashNums={str(x):True for x in range(1,10)}
            for j in range(0,9):
                val=board[i][j]
                if val == ".":
                    continue 

                #check if a row contains duplicate values
                if rowHashNums[val]==True:
                    rowHashNums[val]=False
                else:
                    return False 

                # check if a column contains duplicate values   
                if colHashNums[j][val]==True:
                    colHashNums[j][val]=False
                else:
                    return False

                #get the index of the current box in our hash
                rowIndex,colIndex=i//3, j//3
                if boxHashNums[rowIndex][colIndex][val]==True:
                    boxHashNums[rowIndex][colIndex][val]=False
                else:
                    return False
        return True


                
                

            
                
                
                
