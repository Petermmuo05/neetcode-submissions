class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[None]*len(nums)
        def dfs(index,vals):
            print(index,vals)
            if index>len(vals)-1:
                return 0
            if memo[index]:
                return memo[index]
            else:
                result=max(vals[index]+dfs(index+2,vals),dfs(index+1,vals))
                memo[index]=result
                print(index,result)
                return result
        if len(nums)==1:
            return nums[0]
        first=dfs(0,nums[1:])
        memo=[None]*len(nums[:-1])
        second=dfs(0,nums[:-1])
        return max(first,second)
            

            
        