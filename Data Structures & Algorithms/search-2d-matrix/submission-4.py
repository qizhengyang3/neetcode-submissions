class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0])
        w = len(matrix[0])
        while l < r:
            mid = (l + r) // 2

            if matrix[mid // w][mid % w] == target:
                return True
            elif matrix[mid // w][mid % w] < target:
                l = mid + 1
            else:
                r = mid

        return False