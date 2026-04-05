class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {"}":"{", ")":"(","]":"["}
        stack = []

        for symbol in s:
            if symbol in symbols:
                if stack and stack[-1] == symbols[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)
            
        return True if not stack else False

            
            

            