class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []

        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        
        return False

       