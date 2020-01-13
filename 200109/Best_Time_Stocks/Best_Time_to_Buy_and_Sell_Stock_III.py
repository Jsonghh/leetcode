class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        h1 = h2 = - max(prices) 
        s1 = s2 = 0 
        for price in prices:
            s2,                 h2,                 s1,                 h1 = \
            max(s2, price+h2),  max(h2, -price+s1), max(s1, price+h1),  max(h1, -price) 
        return s2
        



'''
https://www.jiuzhang.com/solution/best-time-to-buy-and-sell-stock-iii/#tag-other-lang-python
'''