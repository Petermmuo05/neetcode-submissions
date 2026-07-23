class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)-1
        while left<right:
            mid=(left+right-1)//2
            if nums[mid]<nums[right]:
                right=mid
            else:
                left=mid+1
        pivot=left
        print(pivot)
        first, end=0, 0
        if nums[0]<nums[-1]:
            first=0
            end=len(nums)-1
        elif target<nums[0]:
            first=pivot
            end=len(nums)-1
        elif target==nums[0]:
            return 0
        else:
            first=0
            end=pivot
        print(first, end)
        while first<=end:
            mid=(first+end)//2
            print(mid, "mid")
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                first=mid+1
            else:
                end=mid-1
        return -1
            
        
