class Solution:
    def __init__(self,):
        self.ans = ''
        
        
    def longestPalindrome(self, s: str) -> str:
        for mid in range(len(s)):
            self.helper(s, mid, mid)
            self.helper(s, mid, mid + 1)
        return self.ans
    
    
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
            
        left += 1
        if right - left > len(self.ans):
            self.ans = s[left:right]
            
        
        
        
    
        
         