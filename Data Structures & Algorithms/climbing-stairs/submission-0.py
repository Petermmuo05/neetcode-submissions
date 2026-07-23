class Solution:
    def climbStairs(self, n: int) -> int:
        memo=[None]*(n+2)
        def dfs(val):
            if memo[val]:
                return memo[val]
            else:
                if val==n:
                    memo[val]=1
                    return 1
                elif val==n+1:
                    memo[val]=0
                    return 0
                else:
                    memo[val]=dfs(val+1)+dfs(val+2)
                    return memo[val]
        return dfs(0)


                

