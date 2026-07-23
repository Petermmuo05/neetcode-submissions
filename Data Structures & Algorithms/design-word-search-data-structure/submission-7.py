class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children={}
            self.isWord=False

    def __init__(self):
        self.root=self.TrieNode()
        
    def addWord(self, word: str) -> None:
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=self.TrieNode()
            node=node.children[char]
        node.isWord=True
        
    def search(self, word: str) -> bool:
        node=self.root
        def dfs(node, index, word):
            if len(list(node.children.keys()))==0 and node.isWord and index<len(word):
                return False
            char=word[index]
            root=node

            if char in node.children:
                root=node.children[char]
                if index==len(word)-1:
                    return root.isWord
                return dfs(root, index+1, word)
            else:
                if char==".":
                    print(node, index, word, len(word)-1)
                    isFound=False
                    if index==len(word)-1:
                        print("broke off")
                        for child in node.children:
                            if node.children[child].isWord:
                                return True
                        return False
                    for child in node.children:
                        if dfs(node.children[child], index+1, word):
                            isFound=True
                    return isFound
                else:
                    return False
        return dfs(node,0,word)
        


