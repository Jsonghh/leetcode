class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            if not word:
                continue
            trie.insert(word)
            
        ans = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.helper(trie.root.children.get(c), board, i, j, ans, set([(i, j)]))
        return sorted(ans)
    
    def helper(self, node, board, i, j, ans, visited):
        if not node:
            return
        if node.is_word and node.word not in ans:
            ans.append(node.word)
#           do not return, keeping searching from board(i, j) using the current node
        moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for di, dj in moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and (ni, nj) not in visited:
                visited.add((ni, nj))
                nc = board[ni][nj]
                self.helper(node.children.get(nc), board, ni, nj, ans, visited)
                visited.remove((ni, nj))
        return
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ''
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word
        
    # def find(self, word):
    #     node = self.root
    #     for c in word:
    #         node = node.children.get(c)
    #         if not node:
    #             return None
    #     if node.is_word:
    #         return word
    #     return None
            
        