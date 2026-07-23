class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums=sorted(nums)
        for index, val in enumerate(nums[:-2]):
            i=index+1
            target=0-val
            if index>0 and val==nums[index-1]:
                print(val, nums[index-1])
                continue
            hashmap={}
            while i<len(nums):
                if nums[i] in hashmap:
                    if [nums[index],nums[hashmap[nums[i]]], nums[i]] not in result:
                        result.append([nums[index],nums[hashmap[nums[i]]], nums[i]])
                else:
                    complementary=target-nums[i]
                    hashmap[complementary]=i
                i+=1
        return result

            