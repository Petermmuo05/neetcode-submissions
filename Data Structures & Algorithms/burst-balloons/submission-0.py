class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp={}
        def dfs(curNums):
            if len(curNums)==1:
                return curNums[0]
            curNumsTuple=tuple(curNums)
            if curNumsTuple in dp:
                return dp[curNumsTuple]
            maxProduct=-float("infinity")
            for index in range(len(curNums)):
                product=curNums[index]
                if index-1>=0:
                    product*=curNums[index-1]
                if index+1<len(curNums):
                    product*=curNums[index+1]
                curNums_copy=curNums.copy()
                curNums_copy.pop(index)
                result=product+dfs(curNums_copy)
                maxProduct=max(maxProduct,result)
            dp[curNumsTuple]=maxProduct
            return maxProduct
        return dfs(nums)