class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fromStart=[]
        fromEnd=[]
        cum=1
        for num in nums:
            cum*=num
            fromStart.append(cum)
        cum=1
        for num in reversed(nums):
            cum*=num
            fromEnd=[cum]+fromEnd
        result=[]
        result.append(fromEnd[1])
        for index in range(1,len(nums)-1):
            res=fromStart[index-1]*fromEnd[index+1]
            result.append(res)
        result.append(fromStart[-2])
        return result

        



        