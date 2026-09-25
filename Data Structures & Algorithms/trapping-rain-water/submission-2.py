class Solution:
    def trap(self, height: List[int]) -> int:
        hashList={x:{"maxLeft":0, "maxRight":0} for x in range(len(height))}
        totalArea=0
        i, j= 0, len(height)-1
        currMaxLeft, currMaxRight=float("-inf"), float("-inf")
        while i<len(height):
            left, right=i, len(height)-i-1
            currMaxLeft, currMaxRight=max(currMaxLeft, height[left]), max(currMaxRight, height[right])
            hashList[left]["maxLeft"], hashList[right]["maxRight"]=currMaxLeft, currMaxRight
            i+=1

        for i in range(1,len(height)-1):
            maxLeftIndex, maxRightIndex=hashList[i-1]["maxLeft"], hashList[i+1]["maxRight"]
            area=max(min(maxLeftIndex, maxRightIndex)-height[i], 0)
            totalArea+=area
        return totalArea




            
            