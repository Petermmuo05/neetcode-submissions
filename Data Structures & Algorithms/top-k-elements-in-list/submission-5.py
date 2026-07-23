class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets=[[] for i in range(len(nums)+1)]
        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num, 0)+1
        print(hashmap, buckets)
        for key, value in hashmap.items():
            buckets[value].append(key)
        result=[]
        index=len(buckets)-1
        while len(result)<k:
            result=buckets[index]+result
            index-=1
        return result[-k:]




        
        

            

