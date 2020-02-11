class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[n]



class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        cur, nex = 0, 1
        
        for _ in range(n):
            cur, nex = nex, nex + cur
            
        return nex
        


class Solution:
    def climbStairs(self, n: int) -> int:
        ans = []
        self.helper(n, ans, [])
        return len(ans)
        
    def helper(self, n, ans, steps):
        if n == 0 and steps:
            ans.append(list(steps))
            return
        
        if n < 0:
            return
        
        rem_steps = [n - 1, n - 2]
        
        for rem in rem_steps:
            steps.append(rem)
            self.helper(rem, ans, steps)
            steps.pop()
        