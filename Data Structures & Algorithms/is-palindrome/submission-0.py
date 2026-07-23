class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed="abcdefghijklmnopqrstuvwxyz0123456789"
        i,j=0,len(s)-1
        while i<j:
            if s[i].casefold() not in allowed or s[j].casefold() not in allowed:
                print(s[i], s[j])
                if s[i].casefold() not in allowed:
                    i+=1
                if s[j].casefold() not in allowed:
                    j-=1
            else:
                if s[i].casefold()!=s[j].casefold():
                    print(s[i], s[j])
                    return False
                i+=1
                j-=1
        return True
        