class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        hashmap={}
        def dfs(index, curSum):
            print(index,curSum)
            if index==len(nums):
                if curSum==target:
                    return 1
                return 0
            if (index, curSum) in hashmap:
                return hashmap[(index, curSum)]
            res=dfs(index+1,curSum+nums[index])
            res+=dfs(index+1,curSum-nums[index])
            hashmap[(index,curSum)]=res
            return res
        return dfs(0,0)

            
            
        