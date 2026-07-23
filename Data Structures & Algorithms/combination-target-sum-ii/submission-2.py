class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(index, cur, total):
            if total==target:
                res.append(cur)
                return
            if total>target or index>=len(candidates):
                return
            dfs(index+1, cur+[candidates[index]], total+candidates[index])
            while index+1<len(candidates) and candidates[index]==candidates[index+1]:
                index+=1
            dfs(index+1, cur, total)
        dfs(0,[],0)
        return res