class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[None]*len(nums)
        def dfs(index):     
            if index>len(nums)-1:
                return 0
            print(index,memo)
            if memo[index]:
                return memo[index]
            val=nums[index]
            skip=dfs(index+1)
            join=dfs(index+2)
            print(skip,join,index)
            maxSum=max(skip,join+val)
            print("maxSum ",maxSum,"index ",index)
            memo[index]=maxSum
            return maxSum
        return dfs(0)
    


            
        