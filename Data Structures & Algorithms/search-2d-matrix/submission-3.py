class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        if top > bottom:
            return False
        row = (top + bottom) // 2
        

        left, right = 0, COLS

        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True
        
        return False



       