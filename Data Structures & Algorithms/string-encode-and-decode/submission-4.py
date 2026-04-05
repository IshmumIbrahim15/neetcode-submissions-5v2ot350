class Solution:

    def encode(self, strs: List[str]) -> str:
        singleStr = ""
        for word in strs:
            singleStr += word +""
        
        return singleStr

    def decode(self, s: str) -> List[str]:
        strs = []
        word = ""
        for char in s:
            if(char == ""):
                strs.append(word)
                word = ""
            else:
                word += char
            
        return strs
                
        
            



