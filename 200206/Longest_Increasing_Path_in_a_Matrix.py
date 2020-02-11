class Solution:
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        memo = [[0] * n for _ in range(m)]
        ans = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
#                  len start with (i, j)
                ans = max(ans, self.helper(matrix, i, j, memo))
                
        return ans
    
    
    def helper(self, matrix, i, j, memo):
        if memo[i][j]:
            return memo[i][j]
        
        for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            ni, nj = i + di, j + dj
            if not ( 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0])):
                continue
            if matrix[ni][nj] <= matrix[i][j]:
                continue
                
            memo[i][j] = max(memo[i][j], self.helper(matrix, ni, nj, memo))
            
        memo[i][j] += 1
        
        return memo[i][j]
            




class Solution:
    def __init__(self,):
        self.ans = 1
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.helper(i, j, [matrix[i][j]], matrix)
                
        return self.ans
    
    
    def helper(self, i, j, path, matrix):
        self.ans = max(self.ans, len(path[:]))
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for di, dj in moves:
            ni, nj = i + di, j + dj
            
            if not(0 <= ni < len(matrix) and 0 <= nj < len(matrix[0])):
                continue
                
            if matrix[ni][nj] <= path[-1]:
                continue
                
            path.append(matrix[ni][nj])
            self.helper(ni, nj, path, matrix)
            path.pop()
            


            