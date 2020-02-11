class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        
        ans = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.helper(matrix, i, j):
                    ans.append([i, j])
                    
        return ans
    
    
    def helper(self, matrix, i, j):
        queue, visited = [(i, j)], set([(i, j)])
        pac, atl = False, False
        while queue:
            ci, cj = queue.pop(0)
            if ci == 0 or cj == 0:
                pac = True
            if ci == len(matrix) - 1 or cj == len(matrix[0]) - 1:
                atl = True
                
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and (ni, nj) not in visited and matrix[ni][nj] <= matrix[ci][cj]:
                    queue.append((ni, nj))
                    visited.add((ni, nj))
                    
        return pac and atl
            
        
        