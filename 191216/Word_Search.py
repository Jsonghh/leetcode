class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return not word
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited.add((i, j))
                if self.helper(board, word, 0, i, j, visited):
                    return True
                visited.remove((i, j))   
        return False
    
    
    def helper(self, board, word, idx, i, j, visited):
        if word[idx] != board[i][j]:
            return False
        if idx == len(word) - 1 and word[idx] == board[i][j]:
            return True
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for di, dj in moves:
            ni, nj = i + di, j + dj
            if (ni, nj) not in visited and 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                visited.add((ni, nj))
                if self.helper(board, word, idx + 1, ni, nj, visited):
                    return True
                visited.remove((ni, nj))
        return False
                