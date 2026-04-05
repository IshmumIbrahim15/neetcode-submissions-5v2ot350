class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums) - 1

        while start < end:
            middle = start + (end - start) // 2

            if nums[middle] < nums[end]:
                end = middle
            else:
                start = middle + 1

        return nums[start]
    





