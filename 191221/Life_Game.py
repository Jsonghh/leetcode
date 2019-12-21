class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = str(board[i][j]) + str(board[i][j])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_nb_cnt = self.find_live_nbs(board, i, j)
                if board[i][j][0] == '0' and live_nb_cnt == 3:
                    board[i][j] = '01'
                if board[i][j][0] == '1':
                    if live_nb_cnt < 2:
                        board[i][j] = '10'
                    if live_nb_cnt > 3:
                        board[i][j] = '10'

                
        for i in range(len(board)):
            for j in range(len(board[0])):
                    board[i][j] = board[i][j][1]
        return board
        
    def find_live_nbs(self, board, i, j):
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        live_nb = 0
        for di, dj in moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj][0] == '1':
                live_nb += 1
        return live_nb
                
        