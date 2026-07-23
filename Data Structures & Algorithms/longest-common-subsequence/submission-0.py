class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        hashmap={}
        def dfs(index1, index2):
            if index1>=len(text1) or index2>=len(text2):
                return 0
            if (index1,index2) in hashmap:
                return hashmap[(index1,index2)]
            res=None
            if text1[index1]==text2[index2]:
                res=1+dfs(index1+1, index2+1)
            else:
                res=max(dfs(index1+1,index2),dfs(index1,index2+1))
            hashmap[(index1,index2)]=res
            return res
        return dfs(0,0)
                
