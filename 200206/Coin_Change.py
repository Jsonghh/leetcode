class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for am in range(coin, amount + 1):
                dp[am] = min(dp[am - coin] + 1, dp[am])
                
        return dp[amount] if dp[amount] != float('inf') else -1
