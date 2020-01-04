class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.min_sum = sum(sum(row) for row in grid)
        memo = {}
        self.helper(grid, 0, 0, memo)
        return memo[(0, 0)]
    
    
    def helper(self, grid, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            memo[(i, j)] = grid[i][j]
            return memo[(i, j)]
        
        cur_min = float('inf')
        for di, dj in [(0, 1), (1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                cur_min = min(cur_min, grid[i][j] + self.helper(grid, ni, nj, memo))
        memo[(i, j)] = cur_min
        return memo[(i, j)]
        
        