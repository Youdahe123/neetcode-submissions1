class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        low = 0
        high = len(matrix) - 1

        while low <= high:# n + n + logm N* 
            mid = (low + high) // 2
            if target in matrix[mid]: # n
                return True
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


        
        