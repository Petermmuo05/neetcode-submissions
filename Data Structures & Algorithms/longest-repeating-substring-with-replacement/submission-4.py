class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap={}
        maxLen=0
        i,j=0,0
        while j<len(s):
            hashmap[s[j]]=hashmap.get(s[j],0)+1
            while j-i-max(hashmap.values())+1>k:
                maxLen=max(maxLen, j-i)
                print(i,j)
                hashmap[s[i]]=hashmap[s[i]]-1
                i+=1
            maxLen=max(maxLen, j-i+1)
            j+=1
        return maxLen
            

            
                