class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def path(pos,cur, visited):
            print(pos, cur, visited,)
            if len(cur)==len(word):
                return True
            nextletter=word[len(cur)]
            print("nextletter", nextletter)
            i,j=pos
            if i>0:
                print("Trying to go up", board[i-1][j], (i-1,j))
                if board[i-1][j].casefold()==nextletter.casefold() and (i-1,j) not in visited:
                    print("Going up")
                    if path((i-1,j),cur+[nextletter],visited+[(i-1,j)]):
                        return True
            if i<len(board)-1:
                print("Trying to go down")
                if board[i+1][j].casefold()==nextletter.casefold() and (i+1,j) not in visited:
                    if path((i+1,j),cur+[nextletter],visited+[(i+1,j)]):
                        return True
            if j>0:
                if board[i][j-1].casefold()==nextletter.casefold() and (i,j-1) not in visited:
                    if path((i,j-1),cur+[nextletter],visited+[(i,j-1)]):
                        return True 
            if j<len(board[i])-1:   
                print("trying to go left", board[i][j+1], nextletter,(i,j+1),board[i][j+1].casefold()==nextletter.casefold(), (i,j+1) not in visited, visited)
                if board[i][j+1].casefold()==nextletter.casefold() and (i,j+1) not in visited:
                    print("going left")
                    if path((i,j+1),cur+[nextletter],visited+[(i,j+1)]):
                        return True
            return False         



        for i,row in enumerate(board):
            for j,col in enumerate(row):
                if col==word[0]:
                    print("first")
                    if path((i,j), [col], [(i,j)]):
                        return True
                    visited=[]
        return False
    

