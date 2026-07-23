class PrefixTree:
    class TrieNode:
        def __init__(self):
            self.children={}
            self.isWord=False
    def __init__(self):
        self.root=self.TrieNode()
        

    def insert(self, word: str) -> None:
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=self.TrieNode()
            node=node.children[char]
        node.isWord=True

    def search(self, word: str) -> bool:
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.isWord

        
    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for char in prefix:
            if char not in node.children:
                return False
            node=node.children[char]
        return True
        
        