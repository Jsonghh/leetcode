class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        sign = '-' if numerator * denominator < 0 else ''
        num, den = abs(numerator), abs(denominator)
        quo, rem = divmod(num, den)
        ans = sign + str(quo) + '.'
        repeat_idx = {}
        
        while rem and rem not in repeat_idx:
            repeat_idx[rem] = len(ans)
            n, rem = divmod(rem * 10, den)
            ans += str(n)
            
        if rem in repeat_idx:
            start_idx = repeat_idx[rem]
            ans = ans[:start_idx] + '(' + ans[start_idx:] + ')'
            
        return ans
            
        