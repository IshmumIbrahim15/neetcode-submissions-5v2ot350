class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        maxArea = 0
        while i < j:
            if heights[i] < heights[j]:
                height = heights[i]
            else:
                height = heights[j]
            
            width = j - i
            area = height * width

            if area > maxArea:
                maxArea = area
            
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        
        return maxArea
            
            


