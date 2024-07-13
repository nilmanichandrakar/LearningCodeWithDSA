class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        x = len(matrix)
        y = len(matrix[0])

        for i in range(x):
            for j in range(y):
                if matrix[i][j] == target:
                    return True

        return False
