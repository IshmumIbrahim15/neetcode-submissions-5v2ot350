class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            if target-nums[i] in hashmap:
                return [hashmap[target-nums[i]],i]
            hashmap[n] = i
