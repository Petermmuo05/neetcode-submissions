class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        reverse={}
        result=[]
        for i in nums:
            hashmap[i]=hashmap.get(i, 0)+1
        for key, value in hashmap.items():
            reverse[value]=reverse.get(value,[])+[key]
        indices=sorted(list(reverse.keys()), reverse=True)[:k]
        print(indices)
        for i in indices:
            result+=reverse[i]
        return result[:k]

        
        

            

