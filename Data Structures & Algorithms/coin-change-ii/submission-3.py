class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        hashmap={}
        coins.sort()
        def dfs(index,amount):
            if index>=len(coins) or amount-coins[index]<0:
                return 0
            curAmount=amount-coins[index]
            if curAmount==0:
                return 1
            if (index, amount) in hashmap:
                return hashmap[(index,amount)]
            left=dfs(index+1,amount)
            right=dfs(index,curAmount)
            res=left+right
            hashmap[(index,amount)]=res
            return res
        if amount==0:
            return 1
        return dfs(0,amount)
            
            
            

 
                
            
