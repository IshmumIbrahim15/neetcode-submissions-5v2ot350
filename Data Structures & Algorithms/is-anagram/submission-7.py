class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersS = 26*[0]
        lettersT = 26*[0]
        #{r:0}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            lettersS[ord(s[i])-ord('a')]+=1
            lettersT[ord(t[i])-ord('a')]+=1
        
        if lettersS == lettersT:
            return True
        
        return False

            
        



        