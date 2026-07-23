class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for value in nums:
            if value in hashmap:
                hashmap[value]+=1
            else:
                hashmap[value]=1
        pairs=list(hashmap.items())
        sortedpairs=sorted(pairs,key=lambda x: x[1])[k*-1:]
        return [x for x,y in sortedpairs]

