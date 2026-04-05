class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for text in strs:
            s+=text
            s+= "ث"
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        start = 0;
        for i in range(len(s)):
            if s[i] == "ث":
                strs.append(s[start:i])
                start = i+1
                
        return strs
        
