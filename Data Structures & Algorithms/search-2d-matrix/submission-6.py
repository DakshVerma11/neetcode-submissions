class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRow = -1
        i = 0
        j = len(matrix) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                targetRow = mid
                break
            elif matrix[mid][0] > target:
                j = mid - 1
            elif matrix[mid][-1]<target:
                i = mid + 1
        print(targetRow)
        
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