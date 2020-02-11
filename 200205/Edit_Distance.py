class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        memo, l1, l2 = {}, len(word1), len(word2)
        self.helper(word1, word2, l1 - 1, l2 - 1, memo)
        
        return memo[(l1 - 1, l2 - 1)]
        
        
    def helper(self, word1, word2, idx1, idx2, memo):
        if (idx1, idx2) in memo:
            return memo[(idx1, idx2)]
        
        if idx1 < 0:
            memo[(idx1, idx2)] = idx2 + 1
            return memo[(idx1, idx2)]
        
        if idx2 < 0:
            memo[(idx1, idx2)] = idx1 + 1
            return memo[(idx1, idx2)]
        
        cnt = float('inf')
        if word1[idx1] == word2[idx2]:
            cnt = self.helper(word1, word2, idx1 - 1, idx2 - 1, memo)
        else:
            cnt = min(self.helper(word1, word2, idx1 - 1, idx2 - 1, memo) + 1,\
                      self.helper(word1, word2, idx1 - 1, idx2 , memo) + 1,\
                      self.helper(word1, word2, idx1, idx2 - 1, memo) + 1)
        
        memo[(idx1, idx2)] = cnt
        
        return memo[(idx1, idx2)]