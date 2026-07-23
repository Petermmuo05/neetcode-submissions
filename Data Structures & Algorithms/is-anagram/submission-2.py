class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1={}
        hashmap2={}
        if len(s)!=len(t):
            return False
        for index, value in enumerate(s):
            if value in hashmap1:
                hashmap1[value]+=1
            else:
                hashmap1[value]=1
        for index, value in enumerate(t):
            if value in hashmap2:
                hashmap2[value]+=1
            else:
                hashmap2[value]=1
        return hashmap1==hashmap2
        
        