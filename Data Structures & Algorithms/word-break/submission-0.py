class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp={}
        def dfs(string):
            print(string)
            if string=="":
                return True
            isFound=False
            if string in dp:
                return dp[string]
            for word in wordDict:
                if string.endswith(word):
                    newString=string[:-len(word)]
                    if dfs(newString):
                        isFound=True
            dp[string]=isFound
            return isFound
        return dfs(s)


                