class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for string in strs:
            res+=str(len(string))+"#"+string
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            print(i)
            print(s[i])
            num=""
            while s[i].isdigit():
                num+=s[i]
                i+=1
            i-=1
            length=int(num)
            newString=s[i+2:i+2+length]
            res.append(newString)
            i=i+2+length
        return res

