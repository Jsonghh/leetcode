class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        steps = [1] * n
        for row in range(1, m):
            for col in range(1, n):
                steps[col] += steps[col - 1]
        return steps[-1]
            
        