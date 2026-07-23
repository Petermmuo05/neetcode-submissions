class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def search(cur, rem):
            
            if len(cur)==len(nums):
                res.append(cur)
                return 
            for ind,val in enumerate(rem):
                newrem=rem.copy()
                newrem.pop(ind)
                search(cur+[val], newrem)
        search([],nums.copy())
        return res
