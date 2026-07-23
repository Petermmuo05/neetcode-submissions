class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(index,cur):
            if index+1<len(nums):
                for val in nums[index+1:]:
                    dfs(index+1, cur+[val])
                    index+=1
            res.append(cur)
        dfs(-1,[])
        return res