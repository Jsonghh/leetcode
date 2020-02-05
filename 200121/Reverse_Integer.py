class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
            
        reverse = 0
        while x:
            reverse = reverse * 10 + x % 10
            x = x // 10
            
        reverse *= sign
            
        if reverse > 2 ** 31 - 1 or reverse < -2 ** 31:
            return 0 
        return reverse