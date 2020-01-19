class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        memo = {}
        self.helper(0, s, memo)
        return memo[0]
    
    
    def helper(self, start, s, memo):
        if start in memo:
            return memo[start]
        
        if start == len(s):
            memo[start] = 1
            return memo[start]
        
        if s[start] == '0':
            memo[start] = 0
            return memo[start]
        
        ways = self.helper(start + 1, s, memo)
        
        if start + 1 < len(s) and int(s[start : start + 2]) <= 26:
            ways += self.helper(start + 2, s, memo)
            
        memo[start] = ways
        
        return memo[start]
    
    
    
'''
class Solution:
    
    def numDecodings(self, s):
        
        if not s or s[0] is '0' : return 0
        
        e0, e1, e2 = 1, 0, 0 
        for c in s:
            e0, e1, e2 = e0 * (c is not '0') + e1 + e2 * (c in '0123456'), e0 * (c is '1'), e0 * (c is '2')
            
        return e0
'''