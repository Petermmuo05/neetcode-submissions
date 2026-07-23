class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i,j=0,k-1
        res=[]
        while j<len(nums):
            maxVal=max(nums[i:j+1])
            res.append(maxVal)
            i+=1
            j+=1
        return res

        