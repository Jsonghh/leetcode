class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
#         check repeated element in 
        row_check = [set() for i in range(9)]
        col_check = [set() for i in range(9)]
        grid_check = [set() for i in range(9)]
        cnt = 81
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    c = board[i][j]
                    cnt -= 1
                    row_check[i].add(c)
                    col_check[j].add(c)
                    grid_check[3 * (i // 3) + j // 3].add(c)
        self.find = False
        self.helper(board, row_check, col_check, grid_check, cnt)
        
        
    def helper(self, board, row, col, grid, cnt):
        if cnt == 0:
            self.find = True
            return
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    continue
                # only try nums on (i, j), do not iterate in the same dfs level
                # can only move to next cell by recursion, due to changes in parameters
                for num in '123456789':
                    if num in row[i] or num in col[j] or num in grid[3 * (i // 3) + j // 3]:
                        continue
                    row[i].add(num)
                    col[j].add(num)
                    grid[3 * (i // 3) + j // 3].add(num)
                    board[i][j] = num
                    #  found a validate number, remaing blank cell cnt - 1
                    self.helper(board, row, col, grid, cnt - 1)
                    #  stop backtracking if board is full
                    if self.find:
                        return
                    row[i].remove(num)
                    col[j].remove(num)
                    grid[3 * (i // 3) + j // 3].remove(num)
                    board[i][j] = '.'
                return
        