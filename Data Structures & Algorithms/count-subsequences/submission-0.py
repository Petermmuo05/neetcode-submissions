class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp={}
        def dfs(index1,index2):
            if index2>=len(t):
                return 1
            if index1>=len(s):
                return 0
            if (index1, index2) in dp:
                return dp[(index1, index2)]
            res=dfs(index1+1, index2)#skip index
            if s[index1]==t[index2]:
                res+=dfs(index1+1, index2+1)#include index
            dp[(index1,index2)]=res
            return res
        return dfs(0,0)
            
            