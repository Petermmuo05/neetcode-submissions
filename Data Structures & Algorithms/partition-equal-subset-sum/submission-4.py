class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums)%2)!=0:
            return False
        half=sum(nums)/2
        dp=[None]*(int(half)+1)
        

        def dfs(amount,visited):
            print(amount,dp,visited)
            if amount==0:
                return True
            if dp[amount]:
                return dp[amount]
            isFound=False
            for index,num in enumerate(nums):
                if num<=amount and index not in visited:
                    print(amount,num)
                    if dfs(amount-num,visited+[index]):
                        isFound=True
            dp[amount]=isFound
            return isFound

        return dfs(int(half),[])
                
        