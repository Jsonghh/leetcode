class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        for char in s:
            num = num * 26 + ord(char) - ord('A') + 1
            
        return num
         


class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        
        while n:
            carry, rem = divmod(n, 26)
            
            if carry and rem == 0:
                carry -= 1
                rem = 26
                
            ans += chr(rem + ord('A') - 1)
            
            n = carry
            
        return str(ans[::-1])
        
         