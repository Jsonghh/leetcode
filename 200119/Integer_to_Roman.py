from collections import OrderedDict
class Solution:
    def intToRoman(self, num: int) -> str:
        d = OrderedDict()
        d = {1000: 'M',
             900: 'CM',
             500: 'D',
             400: 'CD',
             100: 'C',
             90: 'XC',
             50: 'L',
             40: 'XL',
             10: 'X',
             9: 'IX',
             5: 'V',
             4: 'IV',
             1: 'I'}

        ans = ''
        
        for integer, roman in d.items():
            ans += roman * (num // integer)
            num %= integer
            
        return ans
            
        