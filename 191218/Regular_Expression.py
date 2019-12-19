class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.is_match_helper(s, 0, p, 0, {})
    
    
    def is_match_helper(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if len(s) == i:
            return self.can_be_empty(p[j:])
        
        if len(p) == j:
            return False
        
        if j < len(p) - 1 and p[j + 1] == '*':
            is_match = (s[i] == p[j] or p[j] == '.') and \
            self.is_match_helper(s, i + 1, p, j, memo) or\
            self.is_match_helper(s, i, p, j + 2, memo)
        else:
            is_match = (s[i] == p[j] or p[j] == '.') and self.is_match_helper(s, i + 1, p, j + 1, memo)
            
        memo[(i, j)] = is_match
        return is_match
    
    
    def can_be_empty(self, p):
        if len(p) % 2 == 1:
            return False
        for i in range(len(p) // 2):
            if p[i * 2 + 1] != '*':
                return False
        return True