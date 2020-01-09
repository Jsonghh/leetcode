class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.set_flag(matrix, i, j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == float('-inf'):
                    matrix[i][j] = 0
        return 
    
    
    def set_flag(self, matrix, row, col):
        for j in range(len(matrix[0])):
            if matrix[row][j] == 0:
                continue
            matrix[row][j] = float('-inf')
            
        for i in range(len(matrix)):
            if matrix[i][col] == 0:
                continue
            matrix[i][col] = float('-inf')
        