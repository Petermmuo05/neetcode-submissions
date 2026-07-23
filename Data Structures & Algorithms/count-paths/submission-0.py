class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        hashmap={}
        def dfs(position,visited):
            if position in visited:
                return 0
            if position==(m-1,n-1):
                return 1
            r,c=position
            if position in hashmap:
                return hashmap[position]
            res=0
            if r+1 in range(m):
                res+=dfs((r+1,c),visited+[position])
            if c+1 in range(n):
                res+=dfs((r,c+1),visited+[position])
            hashmap[position]=res
            return res
        return dfs((0,0),[])
                
            

        