class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or not k: return 0
        if k > len(prices) // 2:
            return self.unlimited_profits(prices)
            
        max_price = max(prices)
        h = [-max_price for _ in range(k)]
        s = [0 for _ in range(k)]
        
        for price in prices:
            for i in reversed(range(k)):
                
                s[i] = max(s[i], price + h[i])
                
                h[i] = max(h[i], -price if i == 0 else s[i-1] - price)
        
        return s[-1]
    
    def unlimited_profits(self, prices):
        profit = 0
        for idx in range(len(prices)):
            if idx == 0:
                continue
            if prices[idx] - prices[idx - 1] > 0:
                profit += prices[idx] - prices[idx - 1]
                
        return profit