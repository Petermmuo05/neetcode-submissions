class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength=0
        hashmap={}
        i=0
        j=0
        while True:
            if j==len(s):
                maxLength=max(maxLength, j-i)
                break
            if s[j] in hashmap:
                i=hashmap[s[j]]+1
                j=i
                hashmap={}
                continue
            else:
                hashmap[s[j]]=j
                maxLength=max(maxLength, j-i+1)
                j+=1
        return maxLength


                
                