class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            n *= -1
            x = 1 / x
        
        if n == 0:
            return 1
        
        tmp = self.myPow(x, n // 2)
        
        if n % 2 == 0:
            return tmp * tmp
        
        return tmp * tmp * x
        