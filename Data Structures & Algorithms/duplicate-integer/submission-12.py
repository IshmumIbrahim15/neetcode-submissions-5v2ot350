class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countNums = defaultdict()

        for num in nums:
            if num not in countNums:
                countNums[num] = 1
            else:
                return True
        
        return False