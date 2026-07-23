class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        currentBuy=prices[0]
        for index, val in enumerate(prices):
            if val<currentBuy:
                currentBuy=val
            else:
                profit=val-currentBuy
                max_profit=max(profit, max_profit)
        return max_profit