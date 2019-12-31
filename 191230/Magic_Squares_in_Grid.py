class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.helper(grid, i, j):
                    cnt += 1
        return cnt
        
        
    def helper(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i + 2 >= m or j + 2 >= n:
            return False
            
        for row in range(i, i + 3):
            if sum(grid[row][j:j+3]) != 15:                
                return False
            
        for col in range(j, j + 3):
            sum_col = 0
            for row in range(i, i + 3):
                sum_col += grid[row][col]
            if sum_col != 15:
                return False
            
        dia_sum, anti_sum = 0, 0
        idx_sum, idx_diff = i + j + 2, i - j 
        nums = set()
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                if grid[row][col] < 1 or grid[row][col] > 9:
                    return False
                nums.add(grid[row][col])
                if row - col == idx_diff:
                    dia_sum += grid[row][col]
                if col + row == idx_sum:
                    anti_sum += grid[row][col]
        if dia_sum != 15 or anti_sum != 15:
            return False
        
        if len(nums) != 9:
            return False
            
        return True