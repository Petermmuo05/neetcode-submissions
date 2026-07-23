class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for index, value in enumerate(nums):
            if value in hashmap:
                return True
            else:
                hashmap[value]=index
        return False
         