class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix[0])

        rowOfInterest = 0

        while(rowOfInterest < len(matrix)-1):
            if(matrix[rowOfInterest][rowLen-1] == target):
                return True
            elif(matrix[rowOfInterest][rowLen-1] > target):
                break
            else:
                rowOfInterest += 1
        
        i = 0
        start = 0
        print(rowOfInterest)
        end = len(matrix[rowOfInterest]) - 1
        while(start <= end):
            middle = int((start + end)/2)
            if(matrix[rowOfInterest][middle] == target):
                return True
            elif(matrix[rowOfInterest][middle] > target):
                end = middle - 1
            else:
                start = start + 1

        return False

        