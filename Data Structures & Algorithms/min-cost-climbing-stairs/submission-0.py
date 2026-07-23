class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo=[None]*len(cost)
        def dfs(index):
            if index>len(cost)-1:
                return 0
            if memo[index]:
                return memo[index]
            one=dfs(index+1)
            two=dfs(index+2)
            minCost=cost[index]+min(one,two)
            memo[index]=minCost
            return minCost
        zero=dfs(0)
        one=dfs(1)
        return min(zero,one)


            
        