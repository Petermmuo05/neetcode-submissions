class Solution:
    def findMin(self, nums: List[int]) -> int:
        firstNum=nums[0]
        lastNum=nums[-1]
        left, right=0, len(nums)-1
        if len(nums)==1:
            return nums[0]
        if firstNum<lastNum:
            return firstNum
        else:
            while left<=right:
                mid=(left+right+1)//2
                if left==right:
                    return nums[left]
                if nums[mid]<firstNum and nums[mid-1]>nums[mid]:
                    return nums[mid]
                elif nums[mid]>firstNum:
                    left=mid+1
                else:
                    right=mid-1
        return None
                


        