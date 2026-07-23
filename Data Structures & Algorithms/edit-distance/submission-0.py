class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp={}
        def dfs(firstIndex, secondIndex):
            if firstIndex>=len(word1) and secondIndex>=len(word2):
                return 0
            if firstIndex>=len(word1) and secondIndex<len(word2):
                return len(word2)-secondIndex
            if firstIndex<len(word1) and secondIndex>=len(word2):
                return len(word1)-firstIndex

            if (firstIndex, secondIndex) in dp:
                return dp[(firstIndex, secondIndex)]

            res=None
            if word1[firstIndex]==word2[secondIndex]:
                res=dfs(firstIndex+1, secondIndex+1)
                dp[(firstIndex, secondIndex)]=res
                return res
                
            res=min(1+dfs(firstIndex+1, secondIndex),1+dfs(firstIndex, secondIndex+1),1+dfs(firstIndex+1, secondIndex+1))
            dp[(firstIndex, secondIndex)]=res
            return res
        return dfs(0,0)
            