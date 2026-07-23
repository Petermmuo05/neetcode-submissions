class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(index, cur, total):
            print(index, cur, total)
            if total==target:
                res.append(cur.copy())
                return 
            if total>target or index>=len(nums):
                return 
            for val in nums[index:]:
                dfs(index, cur+[val],total+val)
                index+=1
        dfs(0,[],0)
        return res

            