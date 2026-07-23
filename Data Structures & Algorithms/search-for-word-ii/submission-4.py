class Solution:
    class TrieNode:
        def __init__(self):
            self.index=None
            self.children={}
            self.isWord=False
    def __init__(self):
        self.root=self.TrieNode() 

    def insert(self, word: str, index) -> None:
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=self.TrieNode()
                print(node.children[char], char)
            node=node.children[char]
        print()
        node.isWord=True
        node.index=index

    def search(self, word: str) -> bool:
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.isWord

        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res=set()
        for index,word in enumerate(words):
            self.insert(word,index)
            print(self.search(word))
        
        def dfs(pos,node, visited):
            row,col=pos
            print(pos,node.children.get(board[row][col], False),visited)
            print(node.children.keys())
            print(pos)
            if node.children and node.children.get(board[row][col], False) and node.children[board[row][col]].isWord:
                found=words[node.children[board[row][col]].index]
                res.add(found)
            if board[row][col] not in node.children:
                return
            else:
                new_node=node.children[board[row][col]]
                print(new_node, new_node.children.keys())
                if row>0 and (row-1,col) not in visited:
                    dfs((row-1,col),new_node,visited+[(row-1,col)])
                if row<len(board)-1 and (row+1,col) not in visited:
                    dfs((row+1,col),new_node,visited+[(row+1,col)])
                if col>0 and (row,col-1) not in visited:
                    dfs((row,col-1), new_node,visited+[(row,col-1)])
                if col<len(board[row])-1 and (row,col+1) not in visited:
                    dfs((row, col+1), new_node,visited+[(row,col+1)])
            return

        for i,row in enumerate(board):
            for j,col in enumerate(row):
                dfs((i,j),self.root,[(i,j)])
        return list(res)
