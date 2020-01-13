class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Greedy 

        profit = 0
        for idx in range(len(prices)):
            if idx == 0:
                continue
            if prices[idx] - prices[idx - 1] > 0:
                profit += prices[idx] - prices[idx - 1]
                
        return profit
        '''

        if not prices:
            return 0
        profits = 0
        closing = prices[0]
        for opening in prices:
            profits += opening - closing if opening > closing else 0
            closing = opening
        return profits