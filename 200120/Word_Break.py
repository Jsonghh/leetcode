class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        return self.helper(0, set(wordDict), s, memo)
    
    
    def helper(self, start, d, s, memo):
        if start == len(s):
            return True
        if start in memo:
            return memo[start]
        
        for end in range(start + 1, len(s) + 1):
            if self.helper(end, d, s, memo) and s[start : end] in d:
                memo[start] = True
                return memo[start]
        
        memo[start] = False
        return memo[start]