class Solution:
    less20 = ["","One","Two","Three","Four","Five","Six", \
              "Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen", \
              "Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    n_tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    over_thousands = ["","Thousand","Million","Billion"]
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        res = ''
        for i in range(4):
            if num % 1000 != 0:
                res = self.helper(num % 1000) + self.over_thousands[i] + ' ' + res
            num //= 1000
        return res.strip()
    
    
    def helper(self, num):
        if num == 0:
            return ''
        if num < 20:
            return self.less20[num] + ' '
        if num < 100:
            return self.n_tens[num // 10] + ' ' + self.helper(num % 10)
        return self.less20[num // 100] + ' Hundred ' + self.helper(num % 100)
        
   