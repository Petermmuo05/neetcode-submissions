class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        beforeIndexArr=[1]*len(nums)
        afterIndexArr=[1]*len(nums)
        resultArr=[1]*len(nums)
        beforeProduct=afterProduct=1
        for i in range(len(nums)):
            j=len(nums)-1-i
            beforeProduct*=nums[i]
            afterProduct*=nums[j]
            beforeIndexArr[i]=beforeProduct
            afterIndexArr[j]=afterProduct
        for i in range(len(nums)):
            before=beforeIndexArr[i-1] if i-1>=0 else 1
            after=afterIndexArr[i+1] if i+1<=len(nums)-1 else 1
            resultArr[i]=before*after
        return resultArr



            
            


        