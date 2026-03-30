class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top += 1
            elif target < matrix[row][0]:
                bottom -= 1
            else:
                break
        row = (top + bottom) // 2
        left, right = 0, COLS - 1
        while left <= right:
            mid = left + (right - left ) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
            
        
        return False
            
        