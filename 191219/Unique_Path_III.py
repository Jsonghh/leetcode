class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        cnt, si, sj = 0, 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    si, sj = i, j
                if grid[i][j] == 0:
                    cnt += 1
        self.ans, visited = 0, set([(si, sj)])
        self.helper(grid, [(si, sj)], si, sj, visited, cnt)
        return self.ans
    
    
    def helper(self, grid, cur, x, y, v, cnt):
        ei, ej = cur[-1]
        if grid[ei][ej] == 2:
            if cnt == 0:
                self.ans += 1
            return
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in moves:
            nx, ny = x + dx, y +dy
            if not self.validate(grid, nx, ny, v) :
                continue
            if grid[nx][ny] == -1:
                continue
            cur.append((nx, ny))
            if grid[nx][ny] == 0:
                cnt -= 1
            v.add((nx, ny))
            self.helper(grid, cur, nx, ny, v, cnt)
            v.remove((nx, ny))
            cur.pop()
            if grid[nx][ny] == 0:
                cnt += 1
        return
                
    def validate(self, grid, x, y, v):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in v:
            return True
        return False
            
            
                