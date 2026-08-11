class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols= len(matrix[0])

        l = 0 
        r = rows * cols - 1
        while l <= r :
            m = (l + r) // 2
            rows = m // cols
            col = m % cols
            if matrix[rows][col] == target:
                return True
            elif matrix[rows][col] < target:
                l = m + 1
            else:
                r = m - 1
        return False

        