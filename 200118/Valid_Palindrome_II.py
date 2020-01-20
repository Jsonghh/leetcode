class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
            else:
                return self.helper(s, left + 1, right) or self.helper(s, left, right - 1)
            
        return True
    
    def helper(self, s, left, right):
        return s[left: right + 1] == s[left: right + 1][::-1]