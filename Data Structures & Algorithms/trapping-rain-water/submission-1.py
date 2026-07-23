class Solution:
    def trap(self, height: List[int]) -> int:
        fromRight=[0]*len(height)
        fromLeft=[0]*len(height)
        area=[0]*len(height)
        maxVal=-float("inf")
        for index, value in enumerate(height):
            maxVal=max(value, maxVal)
            fromLeft[index]=maxVal
        maxVal=-float("inf")
        for index in range(len(height) - 1, -1, -1):
            value=height[index]
            maxVal=max(value, maxVal)
            fromRight[index]=maxVal
        for index in range(1,len(height)-1):
            water=min(fromRight[index], fromLeft[index])
            amount=max(water-height[index], 0)
            area[index]=amount
        return sum(area)





    



