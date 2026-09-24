class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        nums.sort()
        for i in range(0, len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i-1]==nums[i]:
                continue
            target=nums[i]*-1
            left, right=i+1, len(nums)-1
            while left<right:
                leftVal, rightVal=nums[left], nums[right]
                sumVal=leftVal+rightVal
                if sumVal>target:
                    right-=1
                elif sumVal<target:
                    left+=1
                else:
                    output.append([nums[i], leftVal, rightVal])
                    left+=1
                    right-=1
                    while left< right and nums[left-1]==nums[left]:
                        left+=1
        return output
            

                
        