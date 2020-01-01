class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        
        memo = [-1] * (N + 1)
        memo[0], memo[1] = 0, 1
        self.helper(N, memo)
        return memo[N]
        
    def helper(self, n, memo):
        if memo[n] != -1:
            return memo[n]
        memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        return memo[n]