class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxArea=float("-inf")
        while left<right:
            currArea=min(heights[left], heights[right])*(right-left)
            if currArea>maxArea:
                maxArea=currArea
            if heights[left]>=heights[right]:
                right-=1
            else:
                left+=1
        return maxArea
            
            