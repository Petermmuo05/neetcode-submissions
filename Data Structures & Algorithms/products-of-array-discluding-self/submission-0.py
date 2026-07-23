class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArr=[1]
        rightArr=[1]
        leftCum, rightCum=nums[0], nums[-1]
        left, right=1, len(nums)-2
        output=[]
        while right>=0:
            leftArr.append(leftCum)
            rightArr.append(rightCum)
            leftCum*=nums[left]
            rightCum*=nums[right]
            right-=1
            left+=1
        for i in range(len(leftArr)):
            output.append(leftArr[i]*rightArr[-1*(i+1)])
        return output

        