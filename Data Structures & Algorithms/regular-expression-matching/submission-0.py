class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp={}
        def dfs(i, j):
            print(i,j)
            if (i<len(s) and j>=len(p)):
                return False
            if (i>=len(s) and j<len(p)):
                if j+1==len(p)-1 and p[j+1]=="*":
                    return True
                else:
                    return False
            if i>=len(s) and j>=len(p):
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            res=False
            if j+1<len(p) and p[j+1]=="*":
                if dfs(i,j+2):
                    res=True
                if s[i]==p[j] or p[j]==".":
                    if dfs(i+1,j):
                        res=True
            elif s[i]==p[j] or p[j]==".":
                if dfs(i+1,j+1):
                    res=True
            else:
                return False
            dp[(i,j)]=res
            return res

        return dfs(0,0)

             
            
            
            
