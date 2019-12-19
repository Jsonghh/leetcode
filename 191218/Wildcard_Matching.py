'''
Memorization Search
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.is_match_helper(s, 0, p, 0, {})
    
    
    def is_match_helper(self, s, i, p, j, memo): 
        if (i,j) in memo:
            return memo[(i, j)]
#       if checked all char in source 
        if len(s) == i:
        
            #  every remaning char in pattern should be '*'
            for char in p[j:]:
                if char != '*':
                    return False
            return True
        
#       not all source checked, but all pattern checked
        if len(p) == j:
            return False
        
        if p[j] != '*':
            is_matched = (s[i] == p[j] or p[j] == '?') and \
                self.is_match_helper(s, i + 1, p, j + 1, memo)
        else:
            is_matched = self.is_match_helper(s, i + 1, p, j, memo) or \
                    self.is_match_helper(s, i, p, j + 1, memo)
        memo[(i, j)] = is_matched
        return is_matched        
        
        
        