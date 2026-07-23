class Solution:
    def trap(self, height: List[int]) -> int:
      result=[0]*len(height)
      i,j=0,len(height)-1
      maxLeft=0
      maxRight=height[j]
      while i<=j:
        if maxLeft<=maxRight:
            result[i]=max(0,maxLeft-height[i])
            maxLeft=max(maxLeft, height[i])
            i+=1
        else:
            result[j]=max(0,maxRight-height[j])
            maxRight=max(maxRight, height[j])
            j-=1
      return sum(result)


