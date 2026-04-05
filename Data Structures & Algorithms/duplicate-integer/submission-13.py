class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countNums = set()

        for num in nums:
            if num in countNums:
                return True
            countNums.add(num)
        
        return False