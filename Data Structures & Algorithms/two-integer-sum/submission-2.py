class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index, value in enumerate(nums):
            if value in hashmap:
                return [hashmap[value], index]
            else:
                complement=target-value
                hashmap[complement]=index
        
            
        
            