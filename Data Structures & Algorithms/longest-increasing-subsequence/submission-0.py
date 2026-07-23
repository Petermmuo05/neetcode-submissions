class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        n=len(nums)
        maxLen=-float("infinity")
        for i in range(n-1,-1,-1):
            val=nums[i]
            curMax=-float("infinity")
            for j in range(i,n):
                # print(dp,i,j," ",nums[i],nums[j])
                if nums[j]>val:
                    curMax=max(curMax,dp[j])
            dp[i]=dp[i]+max(curMax,0)
            maxLen=max(maxLen,dp[i])
        return maxLen

        
