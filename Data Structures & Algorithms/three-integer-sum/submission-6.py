class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        result=[]
        print(nums)
        for index,num in enumerate(nums):
            left, right=index+1, len(nums)-1
            if index>0 and num==nums[index-1]:
                continue
            while left<right:
                current=nums[left]+nums[right]
                if current==-num:
                    result.append([num,nums[left], nums[right]])
                    if nums[left+1]==nums[left]:
                        left+=2
                    else:
                        left+=1
                    if nums[right-1]==nums[right]:
                        right-=2
                    else:
                        right-=1
                elif current<-num:
                    if nums[left+1]==nums[left]:
                        left+=2
                    else:
                        left+=1
                else:
                    if nums[right-1]==nums[right]:
                        right-=2
                    else:
                        right-=1
        return result
                
                    

