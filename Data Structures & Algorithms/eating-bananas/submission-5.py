class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = 0
        
        for i in range(len(piles)):
            if(piles[i] > maximum):
                maximum = piles[i]
        
        if(h == len(piles)):
            return maximum
        
        minimum = 1
        k = 1
        target = maximum

        while(minimum <= maximum):
            
            k = int((maximum+minimum)/2)
            hours = 0

            for pile in piles:
                hours += math.ceil(float(pile)/k)
                
            if(hours <= h):
                target = k
                maximum = k - 1
            else:
                minimum = k + 1
            
        return target


