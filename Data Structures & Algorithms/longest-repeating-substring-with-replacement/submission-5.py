class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap={}
        strLen=len(s)
        i,j=0,0
        maxLen=0
        while j<len(s):
            hashmap[s[j]]=hashmap.get(s[j],0)+1
            while (j-i+1)-max(list(hashmap.values()))>k:
                hashmap[s[i]]-=1
                i+=1
            maxLen=max(maxLen, (j-i+1))
            j+=1
        return maxLen
        

        
            

            
                