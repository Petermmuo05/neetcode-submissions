class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [[None for _ in range(n)] for _ in range(n)]
        maxp=-float("infinity")
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if j-i==0:
                    dp[i][j]=nums[i]
                else:
                    dp[i][j]=dp[i+1][j]*nums[i]
                maxp=max(maxp,dp[i][j])
        return maxp
        
                    


