class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if not divisor:
            return float('inf')
        if not dividend:
            return 0
        
        sign = 1 if dividend * divisor > 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        
        ans, times = 0, 0
        while dividend >= divisor:
            tmp = dividend - (divisor << times)
            if tmp >= 0:
                ans += (1 << times)
                times += 1
                dividend = tmp
                
            else:
                times -= 1
                
        MAX, MIN = (1 << 31) - 1, -(1 << 31)
        return sign * ans if MIN <= ans <= MAX else MAX if sign == 1 else MIN
            
      
#         if not divisor:
#             return float('inf')
#         if not dividend:
#             return 0
        
#         sign = 1 if dividend * divisor > 0 else -1
#         dividend, divisor = abs(dividend), abs(divisor)
        
#         tmp = 0
#         for x in range(1, dividend + 1):
#             tmp += divisor
#             if tmp == dividend:
#                 return x * sign
#             if tmp > dividend:
#                 return (x - 1) * sign

      
        