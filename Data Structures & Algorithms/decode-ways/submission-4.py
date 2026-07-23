class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[None]*len(s)
        def dfs(index):
            if index>len(s)-1:
                return 1
            if s[index]=="0":
                print("0")
                return 0
            if index>=len(s)-1:
                return 1
            if dp[index]:
                return dp[index]
            if s[index]=="1" or (s[index]=="2" and index<len(s)-1 and s[index+1] in "0123456"):
                result=dfs(index+1)+dfs(index+2)
                dp[index]=result
                return result
            result=dfs(index+1)
            dp[index]=result
            return result
        return dfs(0)
        