class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        
        INT_MAX, INT_MIN = 2 ** 31 - 1, -2 ** 31
        if not str: 
            return 0
        
        negative = False
        sign_cnt = 0
        
        # check sign and if there are multiple signs
        while str and str[0] in '+-':
            if str[0] == '-':
                negative = True
            str = str[1:]
            sign_cnt += 1
            
        if sign_cnt > 1:
            return 0
        
        # record continuing digits begore invalid letter
        new_str = ''
        for c in str:
            if c.isdigit():
                new_str += c
            else:
                break
        
        # convert string to integer, taking care of big numbers
        num = 0
        for c in new_str:
            num = num * 10 + int(c)
            
        if negative:
            num = -num
            
        if num >= INT_MAX:
            return INT_MAX
        if num <= INT_MIN:
            return INT_MIN
        return num
            
            
            
            
        