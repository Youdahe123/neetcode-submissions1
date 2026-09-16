class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2
            if target in matrix[mid]:
                return True
            if matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


        
        