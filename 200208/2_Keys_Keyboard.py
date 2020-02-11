class Solution:
    def minSteps(self, n: int) -> int:
        ans, op = 0, 2
        while n > 1:
            while n % op == 0:
                ans += op
                n //= op
            op += 1
            
        return ans
        