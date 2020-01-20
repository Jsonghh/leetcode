class Solution:
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        self.helper(s1, s2, s3, memo)
        return memo[(s1, s2)]
      
    
    def helper(self, s1, s2, s3, memo):
        if (s1, s2) in memo:
            return memo[ (s1, s2)]
        
        if len(s1) + len(s2) != len(s3):
            memo[(s1, s2)] = False
            return memo[(s1, s2)]
        
        if not s1:
            memo[(s1, s2)] = s2 == s3
            return memo[(s1, s2)]
        
        if not s2:
            memo[(s1, s2)] = s1 == s3
            return memo[(s1, s2)]
        
        check1, check2 = False, False
        if s1[0] == s3[0]:
            check1 = self.isInterleave(s1[1:], s2, s3[1:])
            
        if s2[0] == s3[0]:
            check2 = self.isInterleave(s1, s2[1:], s3[1:])
            
        memo[(s1, s2)] = check1 or check2
        
        return memo[(s1, s2)]