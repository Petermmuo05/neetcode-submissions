class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for i in range(len(strs)):
            word=strs[i]
            sorted_str="".join(sorted(word))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(word)
                continue
            hashmap[sorted_str]=[word]
        return list(hashmap.values())
        
        