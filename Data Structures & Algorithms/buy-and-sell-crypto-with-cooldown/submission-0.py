class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hashmap={}
        def dfs(index,canBuy):
            if index>=len(prices):
                return 0
            if (index,canBuy) in hashmap:
                return hashmap[(index,canBuy)]
            skip=dfs(index+1,canBuy)
            print(skip,"skip", index)
            res=None
            if canBuy:
                buy=dfs(index+1,False)-prices[index]
                print(buy, "buy", index)
                res=max(buy,skip)
            else:
                sell=dfs(index+2,True)+prices[index]
                print(sell, "sell", index)
                res=max(sell,skip)
            hashmap[(index,canBuy)]=res
            return res
        return dfs(0,True)
            
                