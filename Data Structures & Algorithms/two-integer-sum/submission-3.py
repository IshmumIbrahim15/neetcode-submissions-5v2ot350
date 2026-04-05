class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = defaultdict(int)
        [1,1]
        for i, num in enumerate(nums):
            if target - num in x:
                return[x[target-num], i]
            x[num] = i
        


        
            
        