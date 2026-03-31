class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRow = -1
        
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                targetRow = i
                break
        
        if targetRow == -1:
            return False
        
        i = 0
        j = len(matrix[targetRow]) - 1
        
        while i <= j:
            mid = i + (j - i) // 2
            if matrix[targetRow][mid] == target:
                return True
            elif matrix[targetRow][mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        
        return False