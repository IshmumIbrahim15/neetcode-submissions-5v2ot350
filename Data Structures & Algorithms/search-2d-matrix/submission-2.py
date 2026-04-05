class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                nums.append(matrix[i][j])

        start = 0
        end = len(nums) - 1

        while(start <= end):
            middle = int((start + end)/2)

            if(nums[middle] == target):
                return True
            elif(nums[middle] < target):
                start = middle + 1
            else:
                end = middle - 1
        
        return False

        