class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        if len(board) < 3 or len(board)  < 3:
            return board
        m, n = len(board), len(board[0])
        fall = False
        
        for r in range(m):
            for c in range(n - 2):
                if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:      
                    board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
                    fall = True

                    
        for r in range(m - 2):
            for c in range(n):
                if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:      
                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])
                    fall = True
                    
        if not fall:
            return board

        for c in range(n):
            start = m - 1
            for r in range(m - 1, -1, -1):
                if board[r][c] < 0:
                    continue
                board[start][c] = board[r][c]
                start -= 1
        
            for r in range(start, -1, -1):
                board[r][c] = 0
        
        return self.candyCrush(board)
            


        
                    
            
        