class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        if not grid:
            return 0
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        
        steps = [1] * len(grid[0])  
        
        for i in range(len(grid[0])):
            if grid[0][i] == 1:
                for j in range(i, len(grid[0])):
                    steps[j] = 0
            
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    steps[j] = 0
                    continue
                if j == 0:
                    continue
                steps[j] += steps[j - 1]
        return steps[-1]