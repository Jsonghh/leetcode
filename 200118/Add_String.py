class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        short_num, long_num = sorted([num1, num2], key=len)
        short_num, long_num = list(short_num[::-1]), list(long_num[::-1])
        short_len, long_len = len(short_num), len(long_num)
        carry = 0
        
        for i in range(long_len):
            tmp_sum = int(short_num[i]) + int(long_num[i]) + carry if i < short_len \
                    else int(long_num[i]) + carry
            carry, new_digit = tmp_sum // 10, tmp_sum % 10
            long_num[i] = new_digit
            
        if carry:
            long_num = long_num + [1]
            
        for idx, val in enumerate(long_num):
            long_num[idx] = str(val)
            
        return ''.join(long_num[::-1])
            
            
        
            
            
            