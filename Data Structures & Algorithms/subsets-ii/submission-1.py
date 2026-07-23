class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def search(index,cur):
            print(res, index, cur)
            if index>=len(nums):
                res.append(cur)
                return 
            search(index+1, cur+[nums[index]])
            while index+1<len(nums) and nums[index]==nums[index+1]:
                index+=1
            search(index+1, cur)
        search(0,[])
        return res
