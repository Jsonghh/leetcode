class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        ps, pt = 0, 0
        
        while ps < len(s) and pt < len(t):
            while s[ps] != t[pt]:
                pt += 1
                if pt == len(t):
                    return False
            ps, pt = ps + 1, pt + 1
            
        return ps == len(s)
            
            
        
        