class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hashmap={}
        hashmap[beginWord]=[]

        def compareWords(word1,word2):
            dif=0
            for index, char in enumerate(word1):
                if char!=word2[index]:
                    dif+=1
            return dif==1
        
        for word in wordList:
            hashmap[word]=hashmap.get(word,[])
            for keyWord in hashmap:
                print(word, keyWord)
                if word!=keyWord and compareWords(word, keyWord):
                    hashmap[keyWord]+=[word]
                    hashmap[word]+=[keyWord]

        def dfs(node):
            visited=set()
            print(hashmap)
            que=collections.deque()
            que.append((node,1))
            minDist=float("inf")
            while que:
                curNode,dist=que.pop()
                if curNode in visited:
                    continue
                print(curNode, dist)
                if curNode==endWord:
                    minDist=min(minDist,dist)
                    continue
                for node in hashmap[curNode]:
                    if node not in visited:
                        que.append((node,dist+1))
                visited.add(curNode)
            return 0 if minDist==float("inf") else minDist
        
        return dfs(beginWord)


        