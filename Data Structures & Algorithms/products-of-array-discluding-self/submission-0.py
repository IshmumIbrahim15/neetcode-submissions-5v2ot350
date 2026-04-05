class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = len(nums) * [1]
        after = len(nums) * [1]
        ans = len(nums) * [1]
        
        for i in range(1, len(nums), 1):
            before[i] = before[i-1]*nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            after[i] = after[i+1]*nums[i+1]

        for i in range(len(before)):
            ans[i] = after[i] * before[i]

        return ans

        
            
            
