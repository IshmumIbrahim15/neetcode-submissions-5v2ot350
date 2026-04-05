class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersS = defaultdict(int)
        lettersT = defaultdict(int)
        #{r:0}
        if len(s) != len(t):
            return False
            
        if s == t:
            return True

        for i in range(len(s)):
            lettersS[s[i]]+=1
            lettersT[t[i]]+=1
        
        if lettersS == lettersT:
            return True
        
        return False

            
        



        