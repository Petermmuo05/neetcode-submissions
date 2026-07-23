class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString in hashmap:
                hashmap[sortedString].append(string)
            else:
                hashmap[sortedString]=[string]
        return list(hashmap.values()) 
            